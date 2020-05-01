from mido import Message, MidiFile, MidiTrack
import musthe

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
chord_progression = ['Fmaj7', 'Em7', 'Dm7', 'Cmaj7']


def my_chorus_4_simple(chord_progression, type=1):
    def mode1():
        for chord in chord_progression:
            my_chorus(chord, 4)

    def mode2():
        for chord in chord_progression:
            my_chorus(chord, 1, 1, 100)
            my_chorus(chord, 1, 1)
            my_chorus(chord, 1, 1, 90)
            my_chorus(chord, 0.5, 2)

    def mode3():
        for chord in chord_progression:
            my_chorus(chord, 1, 1, 100)
            my_chorus(chord, 1, 1)
            my_chorus(chord, 1.5, 1, 90)
            my_chorus(chord, 0.5)

    def mode4():
        for chord in chord_progression:
            my_chorus(chord, 2, 1, 100)
            my_chorus(chord, 1.5, 1, 90)
            my_chorus(chord, 0.5)

    def mode5():
        for chord in chord_progression:
            my_chorus(chord, 0.5, 1, 100)
            my_chorus(chord, 0.5, 2)
            my_chorus(chord, 1)
            my_chorus(chord, 0.5, 1, 90)
            my_chorus(chord, 0.5, 2)

    def mode6():
        for chord in chord_progression:
            my_chorus(chord, 0.5, 1, 100)
            my_chorus(chord, 0.5, 2)
            my_chorus(chord, 0.25, 4)
            my_chorus(chord, 0.5, 1, 90)
            my_chorus(chord, 0.5, 1)
            my_chorus(chord, 0.25, 2)

    type_d = {1: mode1, 2: mode2, 3: mode3, 4: mode4, 5: mode5, 6: mode6}
    type_d.get(type)()


def my_chorus_3_simple(chord_progression, type=1):
    def mode1():
        for chord in chord_progression:
            my_chorus(chord, 3)

    def mode2():
        for chord in chord_progression:
            my_chorus(chord, 0.5, 1, 100)
            my_chorus(chord, 1.5)
            my_chorus(chord, 1)

    def mode3():
        for chord in chord_progression:
            my_chorus(chord, 1, 1, 100)
            my_chorus(chord, 0.5, 4)

    def mode4():
        for chord in chord_progression:
            my_chorus(chord, 0.5, 1, 100)
            my_chorus(chord, 1)
            my_chorus(chord, 0.5, 3)

    def mode5():
        for chord in chord_progression:
            my_chorus(chord, 1.5, 1, 100)
            my_chorus(chord, 0.5, 3)

    def mode6():
        for chord in chord_progression:
            my_chorus(chord, 0.75, 1, 100)
            my_chorus(chord, 0.25)
            my_chorus(chord, 0.75)
            my_chorus(chord, 0.25)
            my_chorus(chord, 0.75)
            my_chorus(chord, 0.25)

    type_d = {1: mode1, 2: mode2, 3: mode3, 4: mode4, 5: mode5, 6: mode6}
    type_d.get(type)()


def my_chorus(chord_progression, length, num=1, velocity=80, channel=0):
    """
    :param chord_progression: the chord progression, chould be a list or str
    :param length: the beat
    :param num: the times of repetition
    :param velocity: 0~127,the velocity of chord
    :param channel:0~12
    :return:
    """
    d = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7}
    all_note = []
    if type(chord_progression) == list:  # 如果来的是一个列表，就是几个和弦
        for chord in chord_progression:
            note = []
            if chord[1:len(chord)]:
                temp = musthe.Chord(musthe.Note(chord[0]), chord[1:len(chord)]).notes
            else:
                temp = musthe.Chord(musthe.Note(chord[0])).notes
            for i in range(len(temp)):
                note.append(d[str(temp[i])])
            all_note.append(note)
    else:  # 如果来的只有一个和弦
        note = []
        if chord_progression[1:len(chord_progression)]:
            temp = musthe.Chord(musthe.Note(chord_progression[0]), chord_progression[1:len(chord_progression)]).notes
        else:
            temp = musthe.Chord(musthe.Note(chord_progression[0])).notes
        for i in range(len(temp)):
            note.append(d[str(temp[i])])
        all_note.append(note)
    major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
    base_note = 60
    base_num = 0
    delay = 0
    bpm = 100
    meta_time = 60000 / bpm
    for chord_note in all_note:
        for j in range(num):
            count = 0
            for note in chord_note:
                track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:note]),
                                     velocity=velocity if count else velocity + 10, time=round(delay * meta_time),
                                     channel=channel))
            for note in chord_note:
                track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:note]),
                                     velocity=velocity if count else velocity + 10,
                                     time=0 if count else round(0.96 * meta_time * length),
                                     channel=channel))
                count = count + 1


for i in range(6):
    my_chorus_4_simple(chord_progression, type=i + 1)
# my_chorus_simple(chord_progression, type=4)
mid.save('new_song.mid')
