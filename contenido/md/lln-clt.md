# The Law of Large Numbers and the Central Limit Theorem

*Dariel Amador · Monte Carlo illustration in Python*

Both theorems describe what happens to the sample mean $\bar{x}_n = \frac{1}{n}\sum_{i=1}^n x_i$ of $n$ i.i.d. draws with mean $\mu$ and variance $\sigma^2 < \infty$ as $n$ grows. The LLN says *where* $\bar{x}_n$ goes; the CLT says *how* it fluctuates on the way there.

## Weak Law of Large Numbers

**Theorem.** If $x_1, \dots, x_n$ are i.i.d. with $\mathbb{E}[x_i] = \mu$ and $\operatorname{Var}(x_i) = \sigma^2 < \infty$, then for every $\varepsilon > 0$

$$
\lim_{n \to \infty} P\big( |\bar{x}_n - \mu| > \varepsilon \big) = 0, \qquad \text{that is,} \quad \bar{x}_n \xrightarrow{p} \mu.
$$

**Proof.** By linearity and independence, $\mathbb{E}[\bar{x}_n] = \mu$ and $\operatorname{Var}(\bar{x}_n) = \sigma^2 / n$. Chebyshev's inequality then gives

$$
P\big( |\bar{x}_n - \mu| > \varepsilon \big) \le \frac{\operatorname{Var}(\bar{x}_n)}{\varepsilon^2} = \frac{\sigma^2}{n \varepsilon^2} \xrightarrow[n \to \infty]{} 0. \qquad \blacksquare
$$

### Simulation

Draw $x_i \sim U(0,1)$, so $\mu = 0.5$, and track the running mean along five independent sequences.

```python
rng = np.random.default_rng(42)
n = np.arange(1, 5001)
for _ in range(5):
    u = rng.uniform(0, 1, 5000)
    plt.plot(n, np.cumsum(u) / n)      # running mean x̄_n
plt.axhline(0.5, ls="--")
```

![Running sample means of uniform draws converging to 0.5](contenido/img/lln.png)

Each path wanders for small $n$ and then settles on $0.5$. The horizontal axis is logarithmic: the band around $\mu$ shrinks at rate $1/\sqrt{n}$, exactly the standard deviation $\sigma/\sqrt{n}$ from the proof.

## Central Limit Theorem

**Theorem (Lindeberg–Lévy).** Under the same assumptions,

$$
\sqrt{n}\,\frac{\bar{x}_n - \mu}{\sigma} \xrightarrow{d} \mathcal{N}(0, 1).
$$

**Sketch of proof.** Let $z_i = (x_i - \mu)/\sigma$, with mean 0 and variance 1, and let $\varphi(t)$ be its characteristic function. A second-order expansion gives $\varphi(t) = 1 - \tfrac{t^2}{2} + o(t^2)$. The standardised mean $S_n = \frac{1}{\sqrt{n}} \sum z_i$ has characteristic function

$$
\varphi_{S_n}(t) = \left[ \varphi\!\left( \tfrac{t}{\sqrt{n}} \right) \right]^n = \left[ 1 - \frac{t^2}{2n} + o\!\left(\tfrac{1}{n}\right) \right]^n \xrightarrow[n \to \infty]{} e^{-t^2/2},
$$

which is the characteristic function of $\mathcal{N}(0,1)$. Lévy's continuity theorem completes the argument. $\blacksquare$

### Simulation

The CLT is most convincing when the original distribution is far from normal. Draw from an exponential distribution with $\mu = \sigma = 1$, which is strongly right-skewed, compute the standardised mean 5,000 times for several $n$, and compare with the standard normal density.

```python
for n in [1, 2, 10, 50]:
    x = rng.exponential(1, (5000, n))
    z = (x.mean(axis=1) - 1) / (1 / np.sqrt(n))   # standardised mean
    plt.hist(z, bins=50, density=True)
    plt.plot(grid, stats.norm.pdf(grid))
```

![Standardised means of exponential draws approaching the normal density as n grows](contenido/img/clt.png)

With $n = 1$ we just see the skewed exponential. By $n = 10$ the shape is already close to the bell curve, and at $n = 50$ the remaining skewness is barely visible. The rate at which the skewness disappears is about $1/\sqrt{n}$, which is the content of the Berry–Esseen bound.

## Why it matters in econometrics

The LLN delivers **consistency**: estimators that are sample averages, such as OLS, converge to the population parameter. The CLT delivers **inference**: it justifies normal-based standard errors, $t$-tests and confidence intervals even when the errors themselves are not normal.
