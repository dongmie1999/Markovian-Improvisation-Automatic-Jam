import numpy as np
from hmmlearn import hmm
from mido import Message, MidiFile, MidiTrack
from midi_extended.MidiFileExtended import MidiFileExtended


def hmmmelody():
    startprob = np.array([0.2, 0.3, 0.3, 0.1, 0.1, 0.0, 0.0])
    transmat = np.array([[0.05, 0.30, 0.20, 0.20, 0.10, 0.05, 0.10],
                         [0.30, 0.05, 0.20, 0.20, 0.10, 0.05, 0.10],
                         [0.20, 0.20, 0.05, 0.20, 0.20, 0.05, 0.10],
                         [0.10, 0.30, 0.20, 0.05, 0.20, 0.05, 0.10],
                         [0.10, 0.20, 0.20, 0.30, 0.05, 0.05, 0.10],
                         [0.18, 0.18, 0.18, 0.18, 0.18, 0.10, 0.00],
                         [0.18, 0.18, 0.18, 0.18, 0.18, 0.10, 0.00]])
    means = np.array([[1], [3], [4], [5], [7], [0], [-1]])
    # covariance 为协方差
    covars = .000000000001 * np.tile(np.identity(1), (7, 1, 1))  # 这里identity里的参数1要和means每一行中有的列数对应
    # np.identity 制造对角阵，使用np.tile来把对角阵复制成4行1列1条的三维矩阵

    model = hmm.GaussianHMM(n_components=7, covariance_type="full")
    model.startprob_ = startprob
    model.transmat_ = transmat
    model.means_ = means
    model.covars_ = covars
    # Generate samples
    X, Z = model.sample(50)
    m = []
    for i in range(50):
        temp = int(round(X[i, 0]))
        m.append(temp)
    # print(m)
    return m


def hmmrhythm():
    # Initial population probability
    startprob = np.array([0.15, 0.15, 0.20, 0.20, 0.00, 0.00, 0.20, 0.10, 0.00])
    transmat = np.array([[0.15, 0.15, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10],
                         [0.20, 0.20, 0.20, 0.10, 0.05, 0.05, 0.10, 0.05, 0.05],
                         [0.05, 0.20, 0.20, 0.20, 0.10, 0.05, 0.05, 0.10, 0.05],
                         [0.05, 0.05, 0.20, 0.20, 0.20, 0.10, 0.05, 0.05, 0.10],
                         [0.10, 0.05, 0.05, 0.20, 0.20, 0.20, 0.10, 0.05, 0.05],
                         [0.05, 0.10, 0.05, 0.05, 0.20, 0.20, 0.20, 0.10, 0.05],
                         [0.05, 0.05, 0.10, 0.05, 0.05, 0.20, 0.20, 0.20, 0.10],
                         [0.10, 0.05, 0.05, 0.10, 0.05, 0.05, 0.20, 0.20, 0.20],
                         [0.20, 0.10, 0.05, 0.05, 0.10, 0.05, 0.05, 0.20, 0.20]])
    # The means of each component
    means = np.array([[1], [2], [4], [8], [16], [32], [6], [12], [24]])
    # The covariance of each component # covariance 为协方差
    covars = .000000000001 * np.tile(np.identity(1), (9, 1, 1))  # 这里identity里的参数1要和means每一行中有的列数对应
    # np.identity 制造对角阵，使用np.tile来把对角阵复制成4行1列1条的三维矩阵

    # Build an HMM instance and set parameters
    model = hmm.GaussianHMM(n_components=9, covariance_type="full")
    model.startprob_ = startprob
    model.transmat_ = transmat
    model.means_ = means
    model.covars_ = covars
    # Generate samples
    X, Z = model.sample(32)

    for i in range(32):
        X[i, 0] = int(round(X[i, 0]))
    r = X[:, 0]
    sum = 0
    i = 0
    new_r = []
    while 1 - sum > 0:
        sum += 1 / r[i]
        new_r.append(1 / r[i])
        i += 1
    new_r[i - 1] = 0
    new_r[i - 1] = 1 - np.sum(new_r)
    # print(r[0:i - 1])
    # print(new_r)
    # print(np.sum (new_r))
    return new_r

#
# mid = MidiFile()
# track = MidiTrack()
# # track.name = 'la'
# mid.tracks.append(track)
#
# major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
# base_note = 60
# base_num = 0
# delay = 0
# bpm = 120
# meta_time = 60000 / bpm
# channel = 0
# velocity = 90
# length = 1
#
# melody = melody()
# rhythm = rhythm()
# # mid = MidiFileExtended('../my/all1.mid', type=1, mode='w')
# # mid.add_new_track('Piano', '4/4', 120, 'C', {'3': 0})
# # track = mid.get_extended_track('Piano')
# for i in range(len(rhythm)):
#     m = melody[i]
#     if m > 0:  # 是一个普通音符
#         track.add_note(m, rhythm[i])
#     elif m == 0:  # 是休止符
#         track.add_rest(rhythm[i])
#     else:  # 是延音符
#         track.add_tenuto(rhythm[i])
#
# # track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:1]),
# #                      velocity=90, time=round(delay * meta_time), channel=channel))
# # track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:1]),
# #                      velocity=90, time=round(0.96 * meta_time * length), channel=channel))
#
# mid.save_midi()