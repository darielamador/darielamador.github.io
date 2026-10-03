# OLS is unbiased and consistent

*Dariel Amador · proof and Monte Carlo illustration*

## Setup

Consider the simple linear model

$$
y_i = \beta_0 + \beta_1 x_i + u_i, \qquad i = 1, \dots, n,
$$

with random sampling and the key exogeneity assumption $\mathbb{E}[u_i \mid x_i] = 0$. The OLS slope is

$$
\hat\beta_1 = \frac{\sum_{i}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i}(x_i - \bar{x})^2}.
$$

## Unbiasedness

Substituting the model into the numerator, and using $\sum_i (x_i - \bar{x}) = 0$:

$$
\hat\beta_1 = \beta_1 + \frac{\sum_{i}(x_i - \bar{x})\, u_i}{\sum_{i}(x_i - \bar{x})^2}.
$$

Conditioning on all the regressors $\mathbf{x} = (x_1, \dots, x_n)$, the weights $(x_i - \bar{x}) / \sum_j (x_j - \bar{x})^2$ are constants, so

$$
\mathbb{E}[\hat\beta_1 \mid \mathbf{x}] = \beta_1 + \frac{\sum_{i}(x_i - \bar{x})\, \mathbb{E}[u_i \mid \mathbf{x}]}{\sum_{i}(x_i - \bar{x})^2} = \beta_1.
$$

The law of iterated expectations then gives $\mathbb{E}[\hat\beta_1] = \beta_1$. $\blacksquare$

Unbiasedness holds for **every** sample size, but it only says that the estimator is right on average across samples.

## Consistency

Dividing numerator and denominator by $n$:

$$
\hat\beta_1 = \beta_1 + \frac{\frac{1}{n}\sum_{i}(x_i - \bar{x})\, u_i}{\frac{1}{n}\sum_{i}(x_i - \bar{x})^2}
\;\xrightarrow{p}\; \beta_1 + \frac{\operatorname{Cov}(x, u)}{\operatorname{Var}(x)} = \beta_1.
$$

Each sample average converges to its population counterpart by the Law of Large Numbers, the ratio converges by the continuous mapping theorem (since $\operatorname{Var}(x) > 0$), and $\operatorname{Cov}(x,u) = 0$ follows from $\mathbb{E}[u \mid x] = 0$. $\blacksquare$

Consistency needs only the weaker condition $\operatorname{Cov}(x,u) = 0$, but it is a large-sample property.

## Simulation

Set $\beta_1 = 2$, draw $x_i, u_i \sim \mathcal{N}(0,1)$, and estimate the slope 5,000 times for three sample sizes.

```python
rng = np.random.default_rng(1)
for n in [20, 100, 1000]:
    b = np.empty(5000)
    for r in range(5000):
        x = rng.normal(0, 1, n); u = rng.normal(0, 1, n)
        y = 1 + 2 * x + u
        b[r] = np.cov(x, y, bias=True)[0, 1] / x.var()   # OLS slope
    plt.hist(b, bins=80, density=True, label=f"n = {n}")
```

![Sampling distribution of the OLS slope for n = 20, 100 and 1000](contenido/img/ols.png)

All three distributions are centred on $\beta_1 = 2$ (unbiasedness), and they collapse onto it as $n$ grows (consistency). The spread falls roughly as $1/\sqrt{n}$: going from $n = 100$ to $n = 1000$ cuts the standard deviation by a factor of about 3.
