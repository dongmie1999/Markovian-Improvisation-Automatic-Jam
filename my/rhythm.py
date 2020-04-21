import numpy as np
from hmmlearn import hmm


def rhythm():
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
    print(r[0:i - 1])
    print(new_r)
    # print(np.sum(new_r))
