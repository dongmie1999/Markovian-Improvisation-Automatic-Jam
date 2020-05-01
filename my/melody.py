import numpy as np
from hmmlearn import hmm


def melody():
    startprob = np.array([0.2, 0.3, 0.3, 0.1, 0.1, 0.0, 0.0])
    transmat = np.array([[0.05, 0.30, 0.20, 0.20, 0.10, 0.05, 0.10],
                         [0.30, 0.05, 0.20, 0.20, 0.10, 0.05, 0.10],
                         [0.20, 0.20, 0.05, 0.20, 0.20, 0.05, 0.10],
                         [0.10, 0.30, 0.20, 0.05, 0.20, 0.05, 0.10],
                         [0.10, 0.20, 0.20, 0.30, 0.05, 0.05, 0.10],
                         [0.18, 0.18, 0.18, 0.18, 0.18, 0.10, 0.00],
                         [0.18, 0.18, 0.18, 0.18, 0.18, 0.00, 0.10]])
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

    for i in range(50):
        print(int(round(X[i, 0])), end=',')