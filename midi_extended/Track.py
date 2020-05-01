from mido import Message, MidiTrack, MetaMessage
from fractions import Fraction
import mido
# import traceback
from midi_extended.UtilityBox import *
import musthe
import numpy as np


class TrackExtended(MidiTrack):
    def __init__(self, name='default', time_signature=None, bpm=None, key=None, instruments=None,
                 scale=[0, 2, 2, 1, 2, 2, 2, 1]):
        MidiTrack.__init__(self)
        self.name = name
        self.time_signature = time_signature
        self.bpm = bpm
        self.key = key
        self.instruments = instruments
        self.scale = scale
        self.meta_time = 500  # 其实是60000 / 120，这样设置的时候出来的伴奏的bpm才是对的

        if self.isInitiated():
            self.add_meta_info()

    def initiate_with_track(self, track):
        self.name = track.name
        self.bpm = get_bpm_from_track(track)
        self.key = get_key_from_track(track)
        self.time_signature = get_time_signature_from_track(track)
        self.instruments = get_instruments_from_track(track)

        return self.isInitiated()

    def __str__(self):
        return "Track: " + self.name + \
               " time signature: " + Fraction(self.time_signature).__str__() + \
               " initiated bpm: " + str(self.bpm) + \
               " key: " + self.key

    def isInitiated(self):
        return self.name != 'default' and self.time_signature != None and self.bpm != None and self.key != None and self.instruments != None

    def print_msgs(self):
        for msg in super():
            print(msg)

    def get_name(self):
        return self.name

    def get_time(self):
        return self.time_signature

    def get_bpm(self):
        return self.bpm

    def get_key(self):
        return self.key

    def get_instruments(self):
        return self.instruments

    def set_bpm(self, bpm):
        self.bpm = bpm
        tempo = mido.bpm2tempo(self.bpm)
        super().append(MetaMessage('set_tempo', tempo=tempo, time=0))

    def add_meta_info(self):
        tempo = mido.bpm2tempo(self.bpm)
        numerator = Fraction(self.time_signature).numerator
        denominator = Fraction(self.time_signature).denominator
        super().append(MetaMessage('time_signature', numerator=numerator, denominator=denominator))
        super().append(MetaMessage('set_tempo', tempo=tempo, time=0))
        super().append(MetaMessage('key_signature', key=self.key))
        for channel, program in self.instruments.items():
            super().append(Message('program_change', channel=int(channel), program=program, time=0))

    def add_chord(self, root, name, format, length, root_base=0, channel=3):
        bpm = self.bpm
        scale = [0, 2, 2, 1, 2, 2, 2, 1]
        notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        notes_dict = {}
        for i, note in enumerate(notes):
            notes_dict[note] = 60 + sum(scale[0:i + 1])
        root_note = notes_dict[root] + root_base * 12
        chord = get_chord_arrangement(name)
        time = round(length / len(format) * self.meta_time)

        for dis in format:
            note = root_note + chord[dis]
            super().append(Message('note_on', note=note, velocity=56, time=0, channel=channel))
            super().append(Message('note_off', note=note, velocity=56, time=time, channel=channel))

    def add_bass(self, note, length, base_num=-2, velocity=1.0, channel=6, delay=0):
        bpm = self.bpm
        scale = self.scale
        base_note = 60
        super().append(Message('note_on', note=base_note + base_num * 12 + sum(self.scale[0:note]),
                               velocity=round(80 * velocity), time=round(delay * self.meta_time), channel=channel))
        super().append(Message('note_off', note=base_note + base_num * 12 + sum(self.scale[0:note]),
                               velocity=round(80 * velocity), time=int(round(0.96 * self.meta_time * length)),
                               channel=channel))

    def add_note(self, note, length, modulation=0, base_num=0, delay=0, velocity=90, scale=[0, 2, 2, 1, 2, 2, 2, 1],
                 channel=0, pitch_type=0, tremble_setting=None, bend_setting=None):
        bpm = self.bpm
        base_note = 60 + modulation
        if pitch_type == 0:  # No Pitch Wheel Message
            try:
                super().append(Message('note_on', note=base_note + base_num * 12 + sum(scale[0:note]),
                                       velocity=velocity, time=round(delay * self.meta_time),
                                       channel=channel))
                super().append(Message('note_off', note=base_note + base_num * 12 + sum(scale[0:note]),
                                       velocity=velocity, time=int(round(0.96 * self.meta_time * length)),
                                       channel=channel))
            except IndexError:  # 选中五声音阶时，只有五个音，而hmm生成的最多有七个音
                super().append(Message('note_on', note=base_note + base_num * 12 + sum(scale[0:note - 2]),
                                       velocity=velocity, time=round(delay * self.meta_time),
                                       channel=channel))
                super().append(Message('note_off', note=base_note + base_num * 12 + sum(scale[0:note - 2]),
                                       velocity=velocity, time=int(round(0.96 * self.meta_time * length)),
                                       channel=channel))
        elif pitch_type == 1:  # Tremble
            try:
                pitch = tremble_setting['pitch']
                wheel_times = tremble_setting['wheel_times']
                super().append(Message('note_on', note=base_note + base_num * 12 + sum(scale[0:note]),
                                       velocity=velocity,
                                       time=round(delay * self.meta_time), channel=channel))
                for i in range(wheel_times):
                    super().append(
                        Message('pitchwheel', pitch=pitch,
                                time=round(0.96 * self.meta_time * length / (2 * wheel_times)),
                                channel=channel))
                    super().append(Message('pitchwheel', pitch=0, time=0, channel=channel))
                    super().append(
                        Message('pitchwheel', pitch=-pitch,
                                time=round(0.96 * self.meta_time * length / (2 * wheel_times)),
                                channel=channel))
                super().append(Message('pitchwheel', pitch=0, time=0, channel=channel))
                super().append(Message('note_off', note=base_note + base_num * 12 + sum(scale[0:note]),
                                       velocity=velocity, time=0, channel=channel))
            except:
                print(traceback.format_exc())
        elif pitch_type == 2:  # Bend
            try:
                pitch = bend_setting['pitch']
                PASDA = bend_setting['PASDA']  # Prepare-Attack-Sustain-Decay-Aftermath (Taken the notion of ADSR)
                prepare_rate = PASDA[0] / sum(PASDA)
                attack_rate = PASDA[1] / sum(PASDA)
                sustain_rate = PASDA[2] / sum(PASDA)
                decay_rate = PASDA[3] / sum(PASDA)
                aftermath_rate = PASDA[4] / sum(PASDA)
                super().append(Message('note_on', note=base_note + base_num * 12 + sum(scale[0:note]),
                                       velocity=round(100 * velocity), time=round(delay * self.meta_time),
                                       channel=channel))
                super().append(
                    Message('aftertouch', time=round(0.96 * self.meta_time * length * prepare_rate), channel=channel))
                super().append(
                    Message('pitchwheel', pitch=pitch, time=round(0.96 * self.meta_time * length * attack_rate),
                            channel=channel))
                super().append(
                    Message('aftertouch', time=round(0.96 * self.meta_time * length * sustain_rate), channel=channel))
                super().append(
                    Message('pitchwheel', pitch=0, time=round(0.96 * self.meta_time * length * decay_rate),
                            channel=channel))
                super().append(Message('note_off', note=base_note + base_num * 12 + sum(scale[0:note]),
                                       velocity=velocity,
                                       time=round(0.96 * self.meta_time * length * aftermath_rate),
                                       channel=channel))
            except:
                print(traceback.format_exc())

    def wait(self, time):
        super().append(Message('note_off', time=round(self.meta_time * time)))

    def add_drum(self, name, time, delay=0, velocity=1):
        drum_dict = get_drum_dict()
        try:
            note = drum_dict[name]
        except:
            print(traceback.format_exc())
            return
        super().append(Message('note_on', note=note, velocity=round(64 * velocity), time=delay, channel=9))
        super().append(
            Message('note_off', note=note, velocity=round(64 * velocity), time=int(round(0.96 * self.meta_time * time)),
                    channel=9))

    def my_chorus_4_simple(self, chord_progression, type=1, change=1, circulation=1):
        def mode1():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 4)
            else:
                self.my_chorus_num(chord_progression, 4)

        def mode2():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 1, 1, 80)
                    self.my_chorus(chord, 1, 1)
                    self.my_chorus(chord, 1, 1, 60)
                    self.my_chorus(chord, 0.5, 2)
            else:
                l = len(chord_progression)
                for j in range(circulation):
                    self.my_chorus_num([chord_progression[j % l]], 1, 1, 80)
                    self.my_chorus_num([chord_progression[j % l]], 1, 1)
                    self.my_chorus_num([chord_progression[j % l]], 1, 1, 60)
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 2)

        def mode3():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 1, 1, 80)
                    self.my_chorus(chord, 1, 1)
                    self.my_chorus(chord, 1.5, 1, 60)
                    self.my_chorus(chord, 0.5)
            else:
                l = len(chord_progression)
                for j in range(circulation):
                    self.my_chorus_num([chord_progression[j % l]], 1, 1, 80)
                    self.my_chorus_num([chord_progression[j % l]], 1, 1)
                    self.my_chorus_num([chord_progression[j % l]], 1.5, 1, 60)
                    self.my_chorus_num([chord_progression[j % l]], 0.5)

        def mode4():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 2, 1, 80)
                    self.my_chorus(chord, 1.5, 1, 60)
                    self.my_chorus(chord, 0.5)
            else:
                l = len(chord_progression)
                for j in range(circulation):
                    self.my_chorus_num([chord_progression[j % l]], 2, 1, 80)
                    self.my_chorus_num([chord_progression[j % l]], 1.5, 1, 60)
                    self.my_chorus_num([chord_progression[j % l]], 0.5)

        def mode5():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 0.5, 1, 80)
                    self.my_chorus(chord, 0.5, 2)
                    self.my_chorus(chord, 1)
                    self.my_chorus(chord, 0.5, 1, 60)
                    self.my_chorus(chord, 0.5, 2)
            else:
                l = len(chord_progression)
                for j in range(circulation):
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 1, 80)
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 2)
                    self.my_chorus_num([chord_progression[j % l]], 1)
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 1, 60)
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 2)

        def mode6():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 0.5, 1, 80)
                    self.my_chorus(chord, 0.5, 2)
                    self.my_chorus(chord, 0.25, 4)
                    self.my_chorus(chord, 0.5, 1, 60)
                    self.my_chorus(chord, 0.5, 1)
                    self.my_chorus(chord, 0.25, 2)
            else:
                l = len(chord_progression)
                for j in range(circulation):
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 1, 80)
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 2)
                    self.my_chorus_num([chord_progression[j % l]], 0.25, 4)
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 1, 60)
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 1)
                    self.my_chorus_num([chord_progression[j % l]], 0.25, 2)

        type_d = {1: mode1, 2: mode2, 3: mode3, 4: mode4, 5: mode5, 6: mode6}
        type_d.get(type)()

    def my_chorus_3_simple(self, chord_progression, type=1, change=1, circulation=1):
        def mode1():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 3)
            else:
                self.my_chorus_num(chord_progression, 3)

        def mode2():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 1, 1, 80)
                    self.my_chorus(chord, 1, 2)
            else:
                l = len(chord_progression)
                for j in range(circulation):
                    self.my_chorus_num([chord_progression[j % l]], 1, 1, 80)
                    self.my_chorus_num([chord_progression[j % l]], 1, 2)

        def mode3():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 1, 1, 80)
                    self.my_chorus(chord, 0.5, 4)
            else:
                l = len(chord_progression)
                for j in range(circulation):
                    self.my_chorus_num([chord_progression[j % l]], 1, 1, 80)
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 4)

        def mode4():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 0.5, 1, 80)
                    self.my_chorus(chord, 1)
                    self.my_chorus(chord, 0.5, 3)
            else:
                l = len(chord_progression)
                for j in range(circulation):
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 1, 80)
                    self.my_chorus_num([chord_progression[j % l]], 1)
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 3)

        def mode5():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 1.5, 1, 80)
                    self.my_chorus(chord, 0.5, 3)
            else:
                l = len(chord_progression)
                for j in range(circulation):
                    self.my_chorus_num([chord_progression[j % l]], 1.5, 1, 80)
                    self.my_chorus_num([chord_progression[j % l]], 0.5, 3)

        def mode6():
            if change:
                for chord in chord_progression:
                    self.my_chorus(chord, 0.75, 1, 80)
                    self.my_chorus(chord, 0.25)
                    self.my_chorus(chord, 0.75)
                    self.my_chorus(chord, 0.25)
                    self.my_chorus(chord, 0.75)
                    self.my_chorus(chord, 0.25)
            else:
                l = len(chord_progression)
                for j in range(circulation):
                    self.my_chorus_num([chord_progression[j % l]], 0.75, 1, 80)
                    self.my_chorus_num([chord_progression[j % l]], 0.25)
                    self.my_chorus_num([chord_progression[j % l]], 0.75)
                    self.my_chorus_num([chord_progression[j % l]], 0.25)
                    self.my_chorus_num([chord_progression[j % l]], 0.75)
                    self.my_chorus_num([chord_progression[j % l]], 0.25)

        type_d = {1: mode1, 2: mode2, 3: mode3, 4: mode4, 5: mode5, 6: mode6}
        type_d.get(type)()

    def my_chorus(self, chord_progression, length, num=1, velocity=70, channel=0):
        """
        Specify your chords, length, repetition times and velocity.
        :param chord_progression: the chord progression, chould be a list or str
        :param length: the beat
        :param num: the times of repetition, default 1
        :param velocity: 0~127,the velocity of chord, default 70
        :param channel:0~12, default 0
        """
        d = {'C': 1, 'Db': 2, 'D': 3, 'Eb': 4, 'E': 5, 'F': 6, 'Gb': 7, 'G': 8, 'Ab': 9, 'A': 10, 'Bb': 11, 'B': 12,
             'C#': 2, 'D#': 4, 'F#': 7, 'G#': 9, 'A#': 11}
        all_note = []
        try:
            if type(chord_progression) == list:  # 如果来的是一个列表，就是几个和弦，遍历操作
                for chord in chord_progression:
                    note = []
                    if chord[1:len(chord)]:
                        temp = musthe.Chord(musthe.Note(chord[0]), chord[1:len(chord)]).notes
                        # 得到的结果类似于[Note('F4'), Note('A4'), Note('C5'), Note('E5')]
                    else:
                        temp = musthe.Chord(musthe.Note(chord[0])).notes
                    for i in range(len(temp)):
                        note.append(d[str(temp[i])])  # 这里因为没有考虑和弦音的排列关系，可能实际上使用的和弦的转位
                    all_note.append(note)
            else:  # 如果来的只有一个和弦，直接进行操作
                note = []
                if chord_progression[1:len(chord_progression)]:
                    temp = musthe.Chord(musthe.Note(chord_progression[0]),
                                        chord_progression[1:len(chord_progression)]).notes
                else:
                    temp = musthe.Chord(musthe.Note(chord_progression[0])).notes
                for i in range(len(temp)):
                    note.append(d[str(temp[i])])
                all_note.append(note)
        except ValueError:
            raise ValueError('Chord can not be decoded by musthe.')
        self.my_chorus_num(all_note, length, num, velocity, channel, change=0)  # change为0表示是绝对和弦名称调用

    def my_chorus_num(self, all_note, length, num=1, velocity=70, channel=0, change=1):  # change为1表示是级数调用
        base_note = 60
        base_num = 0
        delay = 0
        for chord_note in all_note:
            for j in range(num):
                count = 0
                for note in chord_note:
                    note = base_note + base_num * 12 + sum(self.scale[0:note]) if change \
                        else base_note + base_num * 12 + note - 1  # 绝对和弦名称时直接加上得到的数字，级数表示和弦需要索引音阶内的音
                    super().append(Message('note_on', note=note, velocity=velocity if count else velocity + 10,
                                           time=round(delay * self.meta_time), channel=channel))
                for note in chord_note:
                    note = base_note + base_num * 12 + sum(self.scale[0:note]) if change \
                        else base_note + base_num * 12 + note - 1
                    super().append(Message('note_off', note=note, velocity=velocity if count else velocity + 10,
                                           time=0 if count else round(0.96 * self.meta_time * length), channel=channel))
                    count = count + 1  # 设第一排为重拍

    def change(self, num, key, mode, count=4):
        """
        change the chord from number to str.
        example: in C major, 1 change to ['C', 'E', 'G']
        :param num: the progression number, should be int from 1~7.
        :param key: char, the first note of scale，could be C D E F G A B.
        :param mode: see doc of class Impromptu.
        :param count: default 3, could be 3, 4 or 5, corresponding triad， seventh chord and hord of the ninthc.
        :return: 1D list, like['C', 'E', 'G']
        """
        d = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7}
        result = []
        try:
            if type(num) == int and 0 < num < 8:
                s = musthe.Scale(musthe.Note(key), mode)
                scale = []
                for i in range(len(s)):
                    scale.append(str(s[i]))
                for i in range(count):
                    try:
                        result.append(d[scale[(num - 1 + 2 * i) % 7][0]])
                    except IndexError:  # 五声音阶的数目比较少，可能会存在超出索引范围的现象
                        result.append(d[scale[(num - 1 + 2 * i) % 5][0]])
            else:
                raise TypeError('num should be int from 1~7.')
        except NameError:
            return self.change(num, key, 'aeolian', count)
        return result

    def add_rest(self, length, velocity=80, channel=0):  # 增加休止符
        super().append(Message('note_off', note=0, velocity=velocity, time=round(0.96 * self.meta_time * length),
                               channel=channel))

    def add_tenuto(self, length):  # 增加延音音符
        off = super().pop()  # list 的最后一个音符的 note_off
        on = super().pop()  # list 的最后一个音符的 note_on
        off.time = round(off.time + 0.96 * self.meta_time * length)
        super().append(on)
        super().append(off)

    def my_bass_4_simple(self, chord_progression, type=1, change=1):
        d = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7}

        # 这里只用7个音，因为add_bass内部已经有对音阶的索引，所以不用12个音

        def mode1():
            for chord in chord_progression:
                self.add_bass(d[chord[0]] if change else int(chord), 0.25)  # 根音
                self.add_rest(0.25)
                self.add_bass(d[chord[0]] if change else int(chord), 0.25)
                self.add_rest(0.5)
                self.add_bass(d[chord[0]] if change else int(chord), 0.25)
                self.add_rest(0.5)
                self.add_bass(d[chord[0]] if change else int(chord), 1)
                self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 1)  # 五音

        def mode2():
            for chord in chord_progression:
                for i in range(16):  # 十六音符根音
                    self.add_bass(d[chord[0]] if change else int(chord), 0.25)

        def mode3():
            for chord in chord_progression:
                self.add_bass(d[chord[0]] if change else int(chord), 0.5)  # 根音
                self.add_bass(d[chord[0]] if change else int(chord), 0.5)
                self.add_rest(0.5)
                self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 0.5)  # 五音
                self.add_bass(d[chord[0]] if change else int(chord), 0.5)
                self.add_bass(d[chord[0]] if change else int(chord), 0.5)
                self.add_rest(0.5)
                self.add_bass((d[chord[0]] - 1) % 7 if change else (int(chord) - 1) % 7, 0.5)  # 七音

        def mode4():
            for chord in chord_progression:  # walking bass
                self.add_bass(d[chord[0]] if change else int(chord), 1)  # 根音
                self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 1)  # 五音
                self.add_bass(d[chord[0]] if change else int(chord), 1)  # 根音
                self.add_bass((d[chord[0]] - 1) % 7 if change else (int(chord) - 1) % 7, 0.75)  # 七音
                self.add_bass((d[chord[0]] - 1) % 7 if change else (int(chord) - 1) % 7, 0.25)  # 七音

        def mode5():
            for chord in chord_progression:
                self.add_bass(d[chord[0]] if change else int(chord), 1)  # 根音
                self.add_bass(d[chord[0]] if change else int(chord), 1)  # 根音
                self.add_bass(d[chord[0]] if change else int(chord), 1.5)  # 根音
                self.add_bass((d[chord[0]] - 1) % 7 if change else (int(chord) - 1) % 7, 0.5)  # 七音

        def mode6():
            i = 0
            for chord in chord_progression:  # slap bass
                if i % 2 == 0:
                    self.add_bass(d[chord[0]] if change else int(chord), 0.25, channel=8)  # 根音
                    self.add_rest(0.5)
                    self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 0.25, channel=8)  # 五音
                    self.add_rest(0.5)
                    self.add_bass(d[chord[0]] if change else int(chord), 0.5, channel=8)  # 根音
                    self.add_bass(d[chord[0]] if change else int(chord), 0.25, channel=8)  # 根音
                    self.add_rest(0.5)
                    self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 0.25, channel=8)  # 五音
                    self.add_rest(0.5)
                    self.add_bass(d[chord[0]] if change else int(chord), 0.5, channel=8)  # 根音
                else:
                    self.add_bass(d[chord[0]] if change else int(chord), 0.25, channel=8)  # 根音
                    self.add_rest(0.5)
                    self.add_bass(d[chord[0]] if change else (int(chord) + 4) % 7, 0.25, channel=8)  # 五音
                    self.add_rest(0.5)
                    self.add_bass(d[chord[0]] if change else int(chord), 0.5, channel=8)  # 根音
                    self.add_bass(d[chord[0]] if change else int(chord), 0.5, channel=8)  # 根音
                    self.add_bass(d[chord[0]] if change else int(chord), 0.5, channel=8)  # 根音
                    self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 0.5, channel=8)  # 五音
                    self.add_bass(d[chord[0]] if change else int(chord), 0.5, channel=8)  # 根音
                i += 1

        def mode7():
            i = 0
            for chord in chord_progression:
                i += 1
                if i % 2:
                    self.add_bass(d[chord[0]] if change else int(chord), 2)  # 根音
                    self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 2)  # 五音
                else:
                    self.add_bass(d[chord[0]] if change else int(chord), 2)  # 根音
                    self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 1)  # 五音
                    self.add_bass(d[chord[0]] if change else int(chord), 1)  # 根音

        type_d = {1: mode1, 2: mode2, 3: mode3, 4: mode4, 5: mode5, 6: mode6, 7: mode7}
        type_d.get(type)()

    def my_bass_3_simple(self, chord_progression, type=1, change=1):
        d = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7}

        def mode1():
            i = 0
            for chord in chord_progression:
                i += 1
                if i % 2:
                    self.add_bass(d[chord[0]] if change else int(chord), 2)  # 根音
                    self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 1)  # 五音
                else:
                    self.add_bass(d[chord[0]] if change else int(chord), 1)  # 根音
                    self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 1)  # 五音
                    self.add_bass(d[chord[0]] if change else int(chord), 1)  # 根音

        def mode2():
            for chord in chord_progression:
                self.add_bass(d[chord[0]] if change else int(chord), 3)  # 根音

        def mode3():
            i = 0
            for chord in chord_progression:
                i += 1
                if i % 2:
                    self.add_bass((d[chord[0]] - 1) % 7 if change else (int(chord) - 1) % 7, 1)  # 七音
                    self.add_bass(d[chord[0]] if change else int(chord), 1)  # 根音
                    self.add_bass((d[chord[0]] + 2) % 7 if change else (int(chord) + 2) % 7, 1)  # 三音
                else:
                    self.add_bass((d[chord[0]] - 1) % 7 if change else (int(chord) - 1) % 7, 1)  # 七音
                    self.add_bass(d[chord[0]] if change else int(chord), 1)  # 根音
                    self.add_bass((d[chord[0]] - 1) % 7 if change else (int(chord) - 1) % 7, 1)  # 七音

        def mode4():
            for chord in chord_progression:
                self.add_bass(d[chord[0]] if change else int(chord), 1)  # 根音
                self.add_bass(d[chord[0]] if change else int(chord), 1.5)  # 根音
                self.add_bass((d[chord[0]] + 4) % 7 if change else int(chord) + 4, 0.5)  # 五音

        def mode5():
            i = 0
            for chord in chord_progression:
                i += 1
                if i % 2:
                    self.add_bass(d[chord[0]] if change else int(chord), 0.5)  # 根音
                    self.add_bass(d[chord[0]] if change else int(chord), 0.5)  # 根音
                    self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 1)  # 五音
                    self.add_bass(d[chord[0]] if change else int(chord), 1)  # 根音
                else:
                    self.add_bass(d[chord[0]] if change else int(chord), 0.5)  # 根音
                    self.add_bass(d[chord[0]] if change else int(chord), 0.5)  # 根音
                    self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 1)  # 五音
                    self.add_bass(d[chord[0]] % 7 if change else int(chord), 0.5)  # 根音
                    self.add_bass((d[chord[0]] - 1) % 7 if change else (int(chord) - 1) % 7, 0.5)  # 七音

        def mode6():
            for chord in chord_progression:
                self.add_bass(d[chord[0]] if change else int(chord), 0.5)  # 根音
                self.add_bass(d[chord[0]] if change else int(chord), 0.5)  # 根音
                self.add_bass((d[chord[0]] + 4) % 7 if change else (int(chord) + 4) % 7, 0.5)  # 五音
                self.add_bass(d[chord[0]] if change else int(chord), 0.5)  # 根音
                self.add_bass((d[chord[0]] - 1) % 7 if change else (int(chord) - 1) % 7, 0.5)  # 五音
                self.add_bass(d[chord[0]] if change else int(chord), 0.5)  # 根音

        def mode7():
            for chord in chord_progression:
                self.add_bass(d[chord[0]] if change else int(chord), 0.25)  # 根音
                self.add_rest(0.25)  # 根音
                self.add_bass(d[chord[0]] if change else int(chord), 0.25)  # 根音
                self.add_rest(0.5)  # 根音
                self.add_bass((d[chord[0]] + 4) % 7 if change else int(chord) + 4, 0.25)  # 五音
                self.add_rest(0.5)  # 根音
                self.add_bass(d[chord[0]] if change else int(chord), 0.5)  # 根音
                self.add_bass((d[chord[0]] - 1) % 7 if change else (int(chord) - 1) % 7, 0.5)  # 根音

        type_d = {1: mode1, 2: mode2, 3: mode3, 4: mode4, 5: mode5, 6: mode6, 7: mode7}
        type_d.get(type)()
