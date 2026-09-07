import numpy as np
import math
import matplotlib.pyplot as plt


# A

def poisson_pmf(k, lambda_):
    return (lambda_ ** k) * np.exp(-lambda_) / math.factorial(k)

def poisson_cdf(k, lambda_):
    return sum(poisson_pmf(i, lambda_) for i in range(k + 1))

print(f"P(N >= 120) = P(N < 120) = {1 - poisson_cdf(119, 250)}")

# C - Simulate and plot accidents on a typical day

accidents = np.random.poisson(250, 1000)
plt.hist(accidents, bins=30, edgecolor='black')

plt.xlabel('Number of Accidents')
plt.ylabel('Frequency')
plt.title('Accidents in a Typical Day')
plt.show()

# D

inter_accident_times = np.random.exponential(1/250, 1000)
plt.hist(inter_accident_times, bins=30, edgecolor='black', density=True)
x = np.linspace(0, 0.02, 100)
plt.plot(x, 250 * np.exp(-250 * x), color='red', label='Exponential PDF')
plt.legend()
plt.xlabel('Time Between Accidents (hours)')
plt.ylabel('Density')
plt.title('Inter-Accident Times')
plt.show()