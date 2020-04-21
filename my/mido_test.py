from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
# track.name = 'la'
mid.tracks.append(track)


# track.append(Message('program_change', program=12, time=0))
# track.append(Message('note_on', note=60, velocity=90, time=500))
# track.append(Message('note_off', note=60, velocity=90, time=500))
# track.append(Message('note_on', note=60, velocity=90, time=500))
# track.append(Message('note_off', note=60, velocity=90, time=500))
# track.append(Message('note_on', note=67, velocity=90, time=500))
# track.append(Message('note_off', note=67, velocity=90, time=500))
# track.append(Message('note_on', note=67, velocity=90, time=500))
# track.append(Message('note_off', note=67, velocity=90, time=500))
# track.append(Message('note_on', note=69, velocity=90, time=500))
# track.append(Message('note_off', note=69, velocity=90, time=500))
# track.append(Message('note_on', note=69, velocity=90, time=500))
# track.append(Message('note_off', note=69, velocity=90, time=500))
# track.append(Message('note_on', note=67, velocity=90, time=500))
# track.append(Message('note_off', note=67, velocity=90, time=500))
# track.append(Message('polytouch', channel=0, note=65, value=0, time=500))

# mid.add_new_track('Melody', self.time_signature, self.bpm, self.key, {'0': 30, '1': 30})

major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
base_note = 60
base_num = 0
delay = 0
bpm = 120
meta_time = 60000 / bpm
channel = 0
velocity = 90
length = 1
track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:1]),
                     velocity=90, time=round(delay * meta_time), channel=channel))
track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:1]),
                     velocity=90, time=round(0.96 * meta_time * length), channel=channel))
track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:2]),
                     velocity=90, time=round(delay * meta_time), channel=channel))
track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:2]),
                     velocity=90, time=round(0.96 * meta_time * length), channel=channel))
track.pop()
track.pop()
track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:2]),
                     velocity=90, time=round(0.96 * meta_time * length), channel=channel))
track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:3]),
                     velocity=90, time=round(delay * meta_time), channel=channel))
track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:3]),
                     velocity=90, time=round(0.96 * meta_time * length), channel=channel))
# length = 1
# for i in range(3):
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:1]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:3]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:5]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:1]),
#                          velocity=90, time=round(0.96 * meta_time * length), channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:3]),
#                          velocity=90, time=0, channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:5]),
#                          velocity=90, time=0, channel=channel))
# length = 0.5
# for i in range(2):
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:1]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:3]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:5]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:1]),
#                          velocity=90, time=round(0.96 * meta_time * length), channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:3]),
#                          velocity=90, time=0, channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:5]),
#                          velocity=90, time=0, channel=channel))
#
# length = 1
# for i in range(3):
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:2]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:4]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:6]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:2]),
#                          velocity=90, time=round(0.96 * meta_time * length), channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:4]),
#                          velocity=90, time=0, channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:6]),
#                          velocity=90, time=0, channel=channel))
# length = 0.5
# for i in range(2):
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:2]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:4]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:6]),
#                          velocity=90, time=round(delay * meta_time), channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:2]),
#                          velocity=90, time=round(0.96 * meta_time * length), channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:4]),
#                          velocity=90, time=0, channel=channel))
#     track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:6]),
#                          velocity=90, time=0, channel=channel))

# def add_note(note, length, base_num=0, delay=0, velocity=1.0, channel=0, pitch_type=0, tremble_setting=None,
#              bend_setting=None):
#     bpm = 120
#     meta_time = 60 * 60 * 10 / bpm
#     major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
#     base_note = 60
#     if pitch_type == 0:  # No Pitch Wheel Message
#         track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:note]),
#                                  velocity=round(64 * velocity), time=round(delay * meta_time), channel=channel))
#         track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:note]),
#                                velocity=round(64 * velocity), time=round(meta_time * length), channel=channel))
#
#
# add_note(1, 1)


mid.save('new_song.mid')
