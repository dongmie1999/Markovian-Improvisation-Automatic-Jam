print("Import start.")
from midi_extended.MidiFileExtended import MidiFileExtended
import my.Q_myhmm
import my.decorator_log
import numpy as np
import time

print("Import end.")


class Impromptu:
    """
    Generate melody automatically base on your chord progression.
    bpm: positive integer，beats per minutes.
    time_signature: the number of beats in each bar, usually in the form of n/m.
        The default rhythmic accompaniment currently only supported 4/m or 3/m.
    key: char, the first note of scale，could be C D E F G A B.
    mode: string, decide the scale of impromptu, could be
          major, dorian, phrygian, lydian, mixolydian, minor, locrian,
          major pentatonic and minor pentatonic.
          ATTENTION: mode decide only your impromptu note,
          do not include the chord.
    file_path: the path and the name of midi file.
    chord_progression: a list of you chords.
    intensity: float between 0 and 1, the parameter of horizontal improvisation and vertical improvisation,
               0 means totally vertical improvisation,
               1 means totally horizontal improvisation.
    repeat: the times that the same chord progression will be repeated.
    """

    def __init__(self):
        self.bpm = 120
        self.time_signature = '4/4'
        self.key = 'C'
        self.mode = 'major'
        self.file_path = '../my/data/song.mid'
        # self.chord_progression = ['Fmaj7', 'Em7', 'Dm7', 'Cmaj7']
        # self.chord_progression = ['Cmaj7', 'Am7', 'F', 'E7']
        self.chord_progression = '4321'
        # 这里得到的列表认为已整理好数据类型，即列表内全是字符（和弦名）或全是级数（GUI 检查）
        self.intensity = 0
        self.repeat = 3
        self.mid = MidiFileExtended(self.file_path, type=1, mode='w')
        self.accompany_type = 1
        self.sw_bass = False
        self.bass_type = 1
        self.silent = False
        self.accompany_tone = 4 if self.silent else 0
        self.note_tone = 26 if self.silent else 0

    @property
    def scale(self):
        d = {'major': [0, 2, 2, 1, 2, 2, 2, 1],
             'dorian': [0, 2, 1, 2, 2, 2, 1, 2],
             'phrygian': [0, 1, 2, 2, 2, 1, 2, 2],
             'lydian': [0, 2, 2, 2, 1, 2, 2, 1],
             'mixolydian': [0, 2, 2, 1, 2, 2, 1, 2],
             'minor': [0, 2, 1, 2, 2, 1, 2, 2],
             'locrian': [0, 1, 2, 2, 1, 2, 2, 2],
             'major_pentatonic': [0, 2, 2, 3, 2, 3],
             'minor_pentatonic': [0, 3, 2, 2, 3, 2]}
        aliases = {'Ionian': 'major', 'aeolian': 'minor'}
        try:
            self._scale = d[self.mode.lower()]
        except KeyError:  # not in d
            try:
                self._scale = d[aliases[self.mode]]
            except KeyError:  # not in aliases
                raise KeyError('Can not find your mode. Please check your key.')
        return self._scale

    @my.decorator_log.decorator_log
    def chorus(self):
        track = self.mid.get_extended_track('Piano')
        track.scale = self.scale
        if type(self.chord_progression) == list:  # 已经是绝对的和弦名称
            for i in range(self.repeat):
                if self.time_signature[0] == '4':
                    track.my_chorus_4_simple(chord_progression=self.chord_progression, type=2)
                else:
                    track.my_chorus_3_simple(chord_progression=self.chord_progression, type=2)
        else:  # 是级数表示的和弦
            change_result = []
            for chord in self.chord_progression:
                change_result.append(track.change(int(chord), self.key, self.mode))
            for i in range(self.repeat):
                if self.time_signature[0] == '4':
                    track.my_chorus_4_simple(change_result, type=1, change=0, circulation=len(self.chord_progression))
                else:
                    track.my_chorus_3_simple(change_result, type=1, change=0, circulation=len(self.chord_progression))
        print("To specify the accompaniment, you can also call function in ./midi_extended/Track.py/my_chorus")
        help(track.my_chorus)

    @my.decorator_log.decorator_log
    def note(self):
        track = self.mid.get_extended_track('Melody')
        # track.print_msgs()
        for j in range(self.repeat):
            print("\r note {} is making...".format(j + 1), end="")
            for chord in self.chord_progression:
                melody = my.Q_myhmm.hmmmelody()
                rhythm = my.Q_myhmm.hmmrhythm()
                multiple = int(self.time_signature[0])
                d = {'C': 1, 'Db': 2, 'D': 3, 'Eb': 4, 'E': 5, 'F': 6, 'Gb': 7, 'G': 8, 'Ab': 9, 'A': 10, 'Bb': 11,
                     'B': 12, 'C#': 2, 'D#': 4, 'F#': 7, 'G#': 9, 'A#': 11}
                if self.intensity:
                    np.random.seed(round(1000000 * time.time()) % 100)  # Seed must be between 0 and 2**32 - 1
                    p = np.array([self.intensity, 1 - self.intensity])
                    if type(self.chord_progression) == list:  # 已经是绝对的和弦名称
                        modulation = np.random.choice([0, d[chord[0]]], p=p.ravel())
                    else:  # 是级数
                        modulation = np.random.choice([0, sum(self.scale[0:int(chord)])], p=p.ravel())
                else:
                    modulation = 0
                # modulation = sum(self.scale[0:d[chord[0]]])
                for i in range(len(rhythm)):
                    m = melody[i]
                    if m > 0:  # 是一个普通音符
                        track.add_note(m, rhythm[i] * multiple, modulation, velocity=110, scale=self.scale, channel=3)
                        # sum(self.scale[0:d[chord[0]]]))
                        # print('add_note', m, rhythm[i]*multiple)
                    elif m == 0:  # 是休止符
                        track.add_rest(rhythm[i] * multiple)
                        # print('add_rest', m, rhythm[i]*multiple)
                    else:  # 是延音符
                        track.add_tenuto(rhythm[i] * multiple)
                        # print('add_tenuto', m, rhythm[i]*multiple)

    def bass(self):
        track = self.mid.get_extended_track('Bass')
        track.scale = self.scale
        if type(self.chord_progression) == list:  # 已经是绝对的和弦名称
            for i in range(self.repeat):
                if self.time_signature[0] == '4':
                    track.my_bass_4_simple(chord_progression=self.chord_progression, type=1)
                else:
                    track.my_bass_3_simple(chord_progression=self.chord_progression, type=1)
        else:  # 是级数表示的和弦
            for i in range(self.repeat):
                if self.time_signature[0] == '4':
                    track.my_bass_4_simple(self.chord_progression, type=i + 1, change=0)
                else:
                    track.my_bass_3_simple(self.chord_progression, type=i + 1, change=0)

    def piano_roll_test(self):
        path = self.file_path
        mid = MidiFileExtended(path, 'r')

        mid.turn_track_into_numpy_matrix('Piano', "../my/data/Piano.npy")
        mid.generate_track_from_numpy_matrix("../my/data/Piano.npy", (288, 128), 'Piano', False, True,
                                             '../my/data/Piano.png')

        mid.turn_track_into_numpy_matrix('Melody', "../my/data/Melody.npy")
        mid.generate_track_from_numpy_matrix("../my/data/Melody.npy", (288, 128), 'Melody', False, True,
                                             '../my/data/Melody.png')

        if self.sw_bass:
            mid.turn_track_into_numpy_matrix('Bass', "../my/data/Bass.npy")
            mid.generate_track_from_numpy_matrix("../my/data/Bass.npy", (288, 128), 'Bass', False, True,
                                                 '../my/data/Bass.png')

    def write_song(self):
        del self.mid
        self.mid = MidiFileExtended(self.file_path, type=1, mode='w')
        self.mid.add_new_track('Piano', self.time_signature, self.bpm, self.key, {'0': 4 if self.silent else 0})  # 4})
        # # 这里的0是30，1也是30的意思，30代表的具体乐器见https://blog.csdn.net/ruyulin/article/details/84103186
        # 在midi_extended/UtilityBox.py中可以看到定义的详细源码（乐理相关）
        self.chorus()

        self.mid.add_new_track('Melody', self.time_signature, self.bpm, self.key, {'3': 26 if self.silent else 0})  # 26
        self.note()

        if self.sw_bass:
            self.mid.add_new_track('Bass', self.time_signature, self.bpm, self.key, {'6': 39 if self.silent else 33,
                                                                                     '7': 35, '8': 36})
            self.bass()


if __name__ == '__main__':
    silence = Impromptu()
    print(silence.scale)
    silence.write_song()
    silence.mid.save_midi()
    silence.piano_roll_test()
    print("Done. Start to play.")
    silence.mid.play_it()

