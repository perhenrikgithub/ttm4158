import math
import numpy as np
import matplotlib.pyplot as plt

# task A

def poisson_pmf(lmbda, x):    
    # this is the same as (e^-λ * λ^x)/(x!)
    # could be computed using scipy.stats.poisson.pmf(x, lmbda) but we implement it manually
    return (math.exp(-lmbda) * (lmbda ** x)) / math.factorial(x)

def poisson_cdf(lmbda, x):
    # this is the same as the sum of pmf from 0 to x
    return sum(poisson_pmf(lmbda, k) for k in range(0, x + 1))

fig, ax = plt.subplots(figsize=(12, 8), nrows=2, ncols=1)

lambdas = [0.05, 2.5, 4, 9]
x_values = np.arange(0, 31)
for lmbda in lambdas:
    pmf_values = [poisson_pmf(lmbda, x) for x in x_values]
    ax[0].plot(x_values, pmf_values, label=f'λ = {lmbda}')

    cdf_values = [poisson_cdf(lmbda, x) for x in x_values]
    ax[1].plot(x_values, cdf_values, label=f'λ = {lmbda}')

ax[0].set_title('Poisson PMF for Different λ Values')
ax[0].set_xlabel('$x$')
ax[0].set_ylabel('$P(X = x)$')
ax[0].set_xticks(x_values)
ax[0].legend()

ax[1].set_title('Poisson CDF for Different λ Values')
ax[1].set_xlabel('$x$')
ax[1].set_ylabel('$P(X ≤ x)$')
ax[1].set_xticks(x_values)
ax[1].legend()

plt.show()


# task B

def exponential_pdf(mu, x):
    if x < 0:
        return 0
    return mu * math.exp(-mu * x)

def exponential_cdf(mu, x):
    if x < 0:
        return 0
    return 1 - math.exp(-mu * x)

fig, ax = plt.subplots(figsize=(12, 8), nrows=2, ncols=1)
mus = [0.1, 1, 10]
x_values = np.linspace(0, 10, 100)
for mu in mus:
    pdf_values = [exponential_pdf(mu, x) for x in x_values]
    ax[0].plot(x_values, pdf_values, label=f'PDF μ = {mu}')
    cdf_values = [exponential_cdf(mu, x) for x in x_values]
    ax[1].plot(x_values, cdf_values, label=f'CDF μ = {mu}')

ax[0].set_title('Exponential PDF for Different μ Values')
ax[0].set_xlabel('$x$')
ax[0].set_ylabel('$f_Y(x)$')
ax[0].legend()

ax[1].set_title('Exponential CDF for Different μ Values')
ax[1].set_xlabel('$x$')
ax[1].set_ylabel('$F_Y(x)$')
ax[1].legend()

plt.show()

print("___ Task B ___")
# Compute mean and variance for exponential distribution
for mu in mus:
    mean = 1 / mu
    variance = 1 / (mu ** 2)
    print(f"For μ = {mu:5.2f}: Mean = {mean:5.2f}, Variance = {variance:5.2f}")

# task C

def W(lmbda, mu):
    if mu <= lmbda:
        raise ValueError("μ < λ")
    return 1 / (mu - lmbda)

print("___ Task C ___")
# Case 1
w1 = W(1.2, 4)
print(f"Case 1: W = {w1}")

# Case 2
w2 = W(0.1, 10)
print(f"Case 2: W = {w2}")

if w1 > w2:
    print("Case 1 has the larger value of W.")
else:
    print("Case 2 has the larger value of W.")

# Fix λ = 1 and plot W as a function of μ for 1.1 ≤ μ ≤ 10
fig, ax = plt.subplots(figsize=(12, 6), nrows=2, ncols=1)
mus = np.linspace(1.1, 10, 100)
ax[0].plot(mus, [W(1, mu) for mu in mus])
ax[0].set_title('W as a function of μ for λ = 1')
ax[0].set_xlabel('$μ$')
ax[0].set_ylabel('$W$')

# Fix μ = 1 and plot W as a function of λ for 0 ≤ λ ≤ 0.9
lambdas = np.linspace(0, 0.9, 100)
ax[1].plot(lambdas, [W(lmbda, 1) for lmbda in lambdas])
ax[1].set_title('W as a function of λ for μ = 1')
ax[1].set_xlabel('$λ$')
ax[1].set_ylabel('$W$')
plt.tight_layout()
plt.show()