import numpy as np
import pandas as pd
from random import seed
from random import random
import matplotlib.pyplot as plt
P = np.array([[0.05, 0.30, 0.20, 0.20, 0.10, 0.07, 0.08],
              [0.30, 0.05, 0.20, 0.20, 0.10, 0.07, 0.08],
              [0.20, 0.20, 0.05, 0.20, 0.20, 0.07, 0.08],
              [0.10, 0.30, 0.20, 0.05, 0.20, 0.07, 0.08],
              [0.10, 0.20, 0.20, 0.30, 0.05, 0.07, 0.08],
              [0.18, 0.18, 0.18, 0.18, 0.18, 0.10, 0.00],
              [0.18, 0.18, 0.18, 0.18, 0.18, 0.00, 0.10]])
state = np.array([0.2, 0.3, 0.3, 0.1, 0.1, 0.0, 0.0])
stateHist = state
dfStateHist = pd.DataFrame(state)
distr_hist = [[0, 0, 0, 0, 0, 0, 0]]
a1 = [];a3 = [];a4 = [];a5 = [];a7 = [];ax = [];a_1 = [];
for x in range(10):
    state = np.dot(state, P)  # 初始分布乘以转移概率矩阵
    a1.append(state[0])
    a3.append(state[1])
    a4.append(state[2])
    a5.append(state[3])
    a7.append(state[4])
    ax.append(state[5])
    a_1.append(state[6])

plt.title('Stationary Analysis')

plt.plot(a1, color='brown', label='1')
plt.plot(a3, color='steelblue', label='b3')
plt.plot(a4, color='skyblue', label='4')
plt.plot(a5, color='salmon', label='5')
plt.plot(a7, color='blueviolet', label='b7')
plt.plot(ax, color='dimgray', label='x')
plt.plot(a_1, color='green', label='-')
plt.legend(loc=1)

plt.xlabel('times')
plt.ylabel('probability')
plt.show()



# import numpy as np
# import pandas as pd
# from random import seed
# from random import random
# import matplotlib.pyplot as plt
# P = np.array([[0.2, 0.7, 0.1],
#               [0.9, 0.0, 0.1],
#               [0.2, 0.8, 0.0]])
# state=np.array([[1.0, 0.0, 0.0]])
# stateHist=state
# dfStateHist=pd.DataFrame(state)
# distr_hist = [[0,0,0]]
# for x in range(50):
#   state=np.dot(state,P)
#   print(state)
#   stateHist=np.append(stateHist,state,axis=0)
#   dfDistrHist = pd.DataFrame(stateHist)
#   dfDistrHist.plot()
# plt.show()