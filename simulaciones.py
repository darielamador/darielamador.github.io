"""Monte Carlo simulations for the econometrics notes. Run: python simulaciones.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
import os

OUT = "contenido/img"
os.makedirs(OUT, exist_ok=True)
A, B, C = "#2f6fd0", "#d9822b", "#2a9d6f"  # readable on light and dark backgrounds
G = "#8a929e"
plt.rcParams.update({
    "figure.facecolor": "none", "axes.facecolor": "none", "savefig.transparent": True,
    "text.color": G, "axes.labelcolor": G, "xtick.color": G, "ytick.color": G,
    "axes.edgecolor": G, "axes.spines.top": False, "axes.spines.right": False,
    "font.size": 11, "legend.frameon": False, "figure.dpi": 150,
})
def save(fig, name):
    fig.tight_layout(); fig.savefig(f"{OUT}/{name}.png", dpi=150); plt.close(fig)

R = 5000  # Monte Carlo replications

# ---------------- LLN and CLT ----------------
def lln_clt():
    rng = np.random.default_rng(42)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    n = np.arange(1, 5001)
    for i in range(5):
        u = rng.uniform(0, 1, 5000)
        ax.plot(n, np.cumsum(u) / n, lw=1, alpha=.85, color=[A, B, C, "#9b5de5", G][i])
    ax.axhline(.5, color=G, ls="--", lw=1)
    ax.set_xscale("log"); ax.set_xlabel("sample size n"); ax.set_ylabel(r"$\bar{x}_n$")
    ax.set_ylim(.2, .8)
    save(fig, "lln")

    fig, axes = plt.subplots(1, 4, figsize=(9, 2.8), sharey=True)
    for ax, k in zip(axes, [1, 2, 10, 50]):
        x = rng.exponential(1, (R, k))
        z = (x.mean(1) - 1) / (1 / np.sqrt(k))
        ax.hist(z, bins=50, density=True, color=A, alpha=.75)
        g = np.linspace(-4, 4, 200); ax.plot(g, stats.norm.pdf(g), color=B, lw=1.8)
        ax.set_title(f"n = {k}", color=G); ax.set_xlim(-4, 5); ax.set_yticks([])
    save(fig, "clt")

# ---------------- 1. OLS unbiased and consistent ----------------
def ols():
    rng = np.random.default_rng(1)
    beta = 2.0
    fig, ax = plt.subplots(figsize=(7, 3.4))
    for n, col in zip([20, 100, 1000], [B, C, A]):
        b = np.empty(R)
        for r in range(R):
            x = rng.normal(0, 1, n); u = rng.normal(0, 1, n)
            y = 1 + beta * x + u
            b[r] = np.cov(x, y, bias=True)[0, 1] / x.var()
        ax.hist(b, bins=80, density=True, histtype="stepfilled", alpha=.45, color=col, label=f"n = {n}  (mean {b.mean():.3f})")
    ax.axvline(beta, color=G, ls="--", lw=1)
    ax.set_xlabel(r"$\hat\beta_1$"); ax.set_yticks([]); ax.legend(); ax.set_xlim(1.2, 2.8)
    save(fig, "ols")

# ---------------- 2. Omitted variable bias ----------------
def ovb():
    rng = np.random.default_rng(2)
    n, b1, b2 = 500, 1.0, 0.8
    rhos = np.linspace(-.8, .8, 9)
    sim, theo = [], []
    for rho in rhos:
        est = np.empty(1000)
        for r in range(1000):
            x1 = rng.normal(0, 1, n)
            x2 = rho * x1 + np.sqrt(1 - rho**2) * rng.normal(0, 1, n)
            y = b1 * x1 + b2 * x2 + rng.normal(0, 1, n)
            est[r] = np.cov(x1, y, bias=True)[0, 1] / x1.var()
        sim.append(est.mean()); theo.append(b1 + b2 * rho)
    fig, ax = plt.subplots(figsize=(7, 3.4))
    ax.plot(rhos, theo, color=B, lw=2, label=r"theory: $\beta_1 + \beta_2\,\mathrm{Cov}(x_1,x_2)/\mathrm{Var}(x_1)$")
    ax.plot(rhos, sim, "o", color=A, label="simulated mean of short-regression $\\tilde\\beta_1$")
    ax.axhline(b1, color=G, ls="--", lw=1)
    ax.set_xlabel(r"correlation between $x_1$ and $x_2$"); ax.set_ylabel(r"$\tilde\beta_1$"); ax.legend(loc="upper left")
    save(fig, "ovb")

# ---------------- 4. Heteroskedasticity ----------------
def hetero():
    rng = np.random.default_rng(4)
    ns = [25, 50, 100, 250, 500, 1000]
    rej_c, rej_r = [], []
    for n in ns:
        rc = rr = 0
        for r in range(3000):
            x = rng.normal(0, 1, n)
            u = rng.normal(0, 1, n) * np.abs(x) * 1.5   # Var(u|x) grows with x^2
            y = 1 + 0 * x + u                           # true slope = 0, so H0 holds
            X = np.column_stack([np.ones(n), x])
            XtXi = np.linalg.inv(X.T @ X)
            b = XtXi @ X.T @ y; e = y - X @ b
            V_c = XtXi * (e @ e / (n - 2))
            meat = (X * e[:, None]**2).T @ X
            V_r = XtXi @ meat @ XtXi * n / (n - 2)       # HC1
            rc += abs(b[1] / np.sqrt(V_c[1, 1])) > 1.96
            rr += abs(b[1] / np.sqrt(V_r[1, 1])) > 1.96
        rej_c.append(rc / 3000); rej_r.append(rr / 3000)
    fig, ax = plt.subplots(figsize=(7, 3.4))
    ax.plot(ns, rej_c, "o-", color=B, label="classical standard errors")
    ax.plot(ns, rej_r, "o-", color=A, label="robust (HC1) standard errors")
    ax.axhline(.05, color=G, ls="--", lw=1); ax.text(ns[-1], .056, "nominal 5%", ha="right", color=G, fontsize=9)
    ax.set_xscale("log"); ax.set_xlabel("sample size n"); ax.set_ylabel("rejection rate of true $H_0$")
    ax.set_ylim(0, max(rej_c) * 1.25); ax.legend()
    save(fig, "hetero")
    return rej_c, rej_r

# ---------------- 5. Gauss-Markov ----------------
def gauss_markov():
    rng = np.random.default_rng(5)
    n, beta = 50, 2.0
    x = np.sort(rng.uniform(0, 10, n))          # fixed regressors
    ols, ends = np.empty(R), np.empty(R)
    k = 10
    for r in range(R):
        y = 1 + beta * x + rng.normal(0, 3, n)
        ols[r] = np.cov(x, y, bias=True)[0, 1] / x.var()
        ends[r] = (y[-k:].mean() - y[:k].mean()) / (x[-k:].mean() - x[:k].mean())
    fig, ax = plt.subplots(figsize=(7, 3.4))
    bins = np.linspace(1.2, 2.8, 70)
    ax.hist(ends, bins=bins, density=True, histtype="stepfilled", alpha=.45, color=B, label=f"grouping estimator  (sd {ends.std():.3f})")
    ax.hist(ols, bins=bins, density=True, histtype="stepfilled", alpha=.55, color=A, label=f"OLS  (sd {ols.std():.3f})")
    ax.axvline(beta, color=G, ls="--", lw=1)
    ax.set_xlabel(r"estimate of $\beta_1$"); ax.set_yticks([]); ax.legend()
    save(fig, "gauss_markov")
    return ols.mean(), ends.mean(), ols.std(), ends.std()

# ---------------- 6. IV and weak instruments ----------------
def iv():
    rng = np.random.default_rng(6)
    n, beta = 500, 1.0
    def run(pi):
        o, v = np.empty(R), np.empty(R)
        for r in range(R):
            z = rng.normal(0, 1, n)
            e = rng.normal(0, 1, n)
            u = .8 * e + .6 * rng.normal(0, 1, n)   # corr(u, e) = 0.8 -> x is endogenous
            x = pi * z + e
            y = beta * x + u
            o[r] = np.cov(x, y, bias=True)[0, 1] / x.var()
            v[r] = np.cov(z, y, bias=True)[0, 1] / np.cov(z, x, bias=True)[0, 1]
        return o, v
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.4))
    for ax, pi, ttl in zip(axes, [.5, .03], ["strong instrument (π = 0.5)", "weak instrument (π = 0.03)"]):
        o, v = run(pi)
        bins = np.linspace(-.5, 2.5, 90)
        ax.hist(v[(v > -.5) & (v < 2.5)], bins=bins, density=True, histtype="stepfilled", alpha=.5, color=A, label=f"IV  (median {np.median(v):.2f}; {np.mean((v<-.5)|(v>2.5)):.0%} off-chart)")
        ax.hist(o, bins=bins, density=True, histtype="stepfilled", alpha=.5, color=B, label=f"OLS  (mean {o.mean():.2f})")
        ax.axvline(beta, color=G, ls="--", lw=1); ax.set_title(ttl, color=G); ax.set_yticks([]); ax.legend(fontsize=9)
        ax.set_xlabel(r"estimate of $\beta$")
    save(fig, "iv")

# ---------------- 7. Spurious regression ----------------
def spurious():
    rng = np.random.default_rng(7)
    T = 200
    def tstat(y, x):
        X = np.column_stack([np.ones(len(x)), x]); XtXi = np.linalg.inv(X.T @ X)
        b = XtXi @ X.T @ y; e = y - X @ b
        s2 = e @ e / (len(x) - 2); return b[1] / np.sqrt(s2 * XtXi[1, 1]), 1 - e.var() / y.var()
    t_rw, t_iid, r2_rw = np.empty(R), np.empty(R), np.empty(R)
    for r in range(R):
        x = np.cumsum(rng.normal(size=T)); y = np.cumsum(rng.normal(size=T))
        t_rw[r], r2_rw[r] = tstat(y, x)
        t_iid[r], _ = tstat(rng.normal(size=T), rng.normal(size=T))
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.4))
    rng2 = np.random.default_rng(70)
    x = np.cumsum(rng2.normal(size=T)); y = np.cumsum(rng2.normal(size=T))
    axes[0].plot(x, color=A, lw=1.4, label="$x_t$"); axes[0].plot(y, color=B, lw=1.4, label="$y_t$")
    axes[0].set_title("two independent random walks", color=G); axes[0].set_xlabel("t"); axes[0].legend()
    bins = np.linspace(-30, 30, 90)
    axes[1].hist(t_iid[abs(t_iid) < 30], bins=bins, density=True, histtype="stepfilled", alpha=.6, color=C, label=f"i.i.d. series  (reject {np.mean(abs(t_iid)>1.96):.0%})")
    axes[1].hist(t_rw[abs(t_rw) < 30], bins=bins, density=True, histtype="stepfilled", alpha=.5, color=B, label=f"random walks  (reject {np.mean(abs(t_rw)>1.96):.0%})")
    axes[1].set_title("t-statistic of the slope", color=G); axes[1].set_yticks([]); axes[1].legend(fontsize=9)
    save(fig, "spurious")
    return np.mean(abs(t_rw) > 1.96), np.mean(abs(t_iid) > 1.96), np.median(r2_rw)

if __name__ == "__main__":
    lln_clt(); ols(); ovb()
    print("hetero", hetero())
    print("gm", gauss_markov())
    iv()
    print("spurious", spurious())
