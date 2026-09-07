# 

import matplotlib.pyplot as plt
import numpy as np

def P_success(N, p):
    return N * p * (1 - p) ** (N - 1)

Ns = np.arange(5, 101, 5)
plt.plot(Ns, P_success(Ns, 0.05), label='p=0.05')
plt.axvline(x=20, color='r', linestyle='--', label='N=20')

plt.xlabel('$N$')
plt.ylabel('$P_{succ}$')
plt.title('Utilisation vs. N')
plt.legend()
plt.show()