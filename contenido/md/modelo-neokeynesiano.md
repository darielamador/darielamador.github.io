# Full derivation of the New Keynesian model

*Dariel Amador · based on Galí (2015), ch. 3*

This note derives the two core blocks of the basic New Keynesian model: the **dynamic IS curve**, from the households' problem, and the **New Keynesian Phillips Curve (NKPC)**, from the firms' price-setting problem under Calvo-type price rigidities.

## 1. Households

### Intertemporal problem

The representative household chooses consumption, hours worked and bond holdings to maximise expected discounted utility:

$$
\max_{\{C_t,\,N_t,\,B_t\}} \; \mathbb{E}_0 \sum_{t=0}^{\infty} \beta^t \left( \frac{C_t^{1-\sigma}}{1-\sigma} - \frac{N_t^{1+\varphi}}{1+\varphi} \right)
\quad \text{s.t.} \quad P_t C_t + B_t \le W_t N_t + (1+i_{t-1}) B_{t-1} + \Pi_t \tag{1}
$$

The Lagrangian, with one multiplier $\lambda_t$ per period, is:

$$
\mathcal{L} = \mathbb{E}_0 \sum_{t=0}^{\infty} \beta^t \left[ \frac{C_t^{1-\sigma}}{1-\sigma} - \frac{N_t^{1+\varphi}}{1+\varphi} + \lambda_t \big( W_t N_t + (1+i_{t-1}) B_{t-1} + \Pi_t - P_t C_t - B_t \big) \right] \tag{2}
$$

### First-order conditions

$$
\begin{aligned}
\frac{\partial \mathcal{L}}{\partial C_t} = 0 &\iff C_t^{-\sigma} - \lambda_t P_t = 0 \iff \frac{C_t^{-\sigma}}{P_t} = \lambda_t \\[4pt]
\frac{\partial \mathcal{L}}{\partial N_t} = 0 &\iff -N_t^{\varphi} + \lambda_t W_t = 0 \iff \frac{N_t^{\varphi}}{W_t} = \lambda_t \\[4pt]
\frac{\partial \mathcal{L}}{\partial B_t} = 0 &\iff -\lambda_t + \beta\, \mathbb{E}_t\!\left[ \lambda_{t+1} (1+i_t) \right] = 0 \iff \beta (1+i_t)\, \mathbb{E}_t[\lambda_{t+1}] = \lambda_t
\end{aligned}
\tag{3–5}
$$

Because $\beta^t$ multiplies every term dated $t$, differentiating with respect to $B_t$ leaves a single $\beta$ (not $\beta^t$): a bond bought in $t$ pays off in $t+1$, one period ahead.

### Euler equation

Substituting (3) into (5), at $t$ and at $t+1$:

$$
\frac{C_t^{-\sigma}}{P_t} = \beta (1+i_t)\, \mathbb{E}_t\!\left[ \frac{C_{t+1}^{-\sigma}}{P_{t+1}} \right]
\iff C_t^{-\sigma} = \beta (1+i_t)\, \mathbb{E}_t\!\left[ C_{t+1}^{-\sigma} \frac{P_t}{P_{t+1}} \right] \tag{6–8}
$$

Multiplying both sides by $P_t$ lets us introduce inflation. Defining $\pi_{t+1} = \dfrac{P_{t+1} - P_t}{P_t}$:

$$
1 + \pi_{t+1} = \frac{P_{t+1}}{P_t} \iff \frac{1}{1+\pi_{t+1}} = \frac{P_t}{P_{t+1}} \tag{9–12}
$$

Plugging (12) into (8) and dividing by $C_t^{-\sigma}$:

$$
1 = \beta\, \mathbb{E}_t\!\left[ \left( \frac{C_{t+1}}{C_t} \right)^{-\sigma} \frac{1+i_t}{1+\pi_{t+1}} \right]
$$

### Log-linearisation

We take logs (ignoring second-order terms such as Jensen's inequality) and use $\ln(1+x) \approx x$ for small $x$. With $c_t \equiv \ln C_t$ and $\rho \equiv -\ln \beta$:

$$
\begin{aligned}
0 &= \ln \beta - \sigma \left( \mathbb{E}_t[c_{t+1}] - c_t \right) + \ln(1+i_t) - \mathbb{E}_t[\ln(1+\pi_{t+1})] \\
0 &= -\rho - \sigma \left( \mathbb{E}_t[c_{t+1}] - c_t \right) + i_t - \mathbb{E}_t[\pi_{t+1}]
\end{aligned}
\tag{13–17}
$$

Solving for $c_t$:

$$
\boxed{\; c_t = \mathbb{E}_t[c_{t+1}] - \frac{1}{\sigma} \left( i_t - \mathbb{E}_t[\pi_{t+1}] - \rho \right) \;} \tag{19}
$$

Equation (19) is the **dynamic IS curve**: current consumption falls when the expected real interest rate, $i_t - \mathbb{E}_t[\pi_{t+1}]$, exceeds the discount rate $\rho$. In equilibrium, with $Y_t = C_t$, it can be written in terms of output.

## 2. Firms

Each firm produces a differentiated variety and, with probability $\theta$, cannot adjust its price in a given period (Calvo, 1983). When it can, it chooses the optimal price $P_t^*$ that maximises the present value of profits while that price remains in effect:

$$
\max_{P_t^*} \; \sum_{k=0}^{\infty} \theta^k\, \mathbb{E}_t \left[ Q_{t,t+k} \left( P_t^* Y_{t+k|t} - \Psi_{t+k}(Y_{t+k|t}) \right) \right]
\quad \text{s.t.} \quad Y_{t+k|t} = \left( \frac{P_t^*}{P_{t+k}} \right)^{-\varepsilon} Y_{t+k} \tag{20}
$$

where $Q_{t,t+k} = \beta^k (C_{t+k}/C_t)^{-\sigma}(P_t/P_{t+k})$ is the stochastic discount factor and $\Psi$ is the cost function. Substituting demand into the objective gives an unconstrained problem:

$$
\max_{P_t^*} \; \sum_{k=0}^{\infty} \theta^k\, \mathbb{E}_t \left[ Q_{t,t+k} \left( (P_t^*)^{1-\varepsilon} P_{t+k}^{\varepsilon} Y_{t+k} - \Psi_{t+k}\!\left( \left( \frac{P_t^*}{P_{t+k}} \right)^{-\varepsilon} Y_{t+k} \right) \right) \right] \tag{21–22}
$$

### First-order condition

Using $\dfrac{\partial Y_{t+k|t}}{\partial P_t^*} = -\varepsilon \dfrac{Y_{t+k|t}}{P_t^*}$ and defining nominal marginal cost $\psi_{t+k|t} \equiv \Psi'_{t+k}(Y_{t+k|t})$:

$$
\sum_{k=0}^{\infty} \theta^k\, \mathbb{E}_t \left[ Q_{t,t+k} \left( (1-\varepsilon) Y_{t+k|t} + \varepsilon\, \psi_{t+k|t} \frac{Y_{t+k|t}}{P_t^*} \right) \right] = 0 \tag{23–28}
$$

Multiplying by $P_t^* / (\varepsilon - 1)$ and rearranging:

$$
\sum_{k=0}^{\infty} \theta^k\, \mathbb{E}_t \left[ Q_{t,t+k}\, Y_{t+k|t} \left( P_t^* - \mathcal{M}\, \psi_{t+k|t} \right) \right] = 0,
\qquad \mathcal{M} \equiv \frac{\varepsilon}{\varepsilon - 1} \tag{32}
$$

Solving for the optimal price:

$$
\boxed{\; P_t^* = \frac{\varepsilon}{\varepsilon - 1} \cdot
\frac{\mathbb{E}_t \sum_{k=0}^{\infty} \theta^k\, Q_{t,t+k}\, Y_{t+k|t}\, \psi_{t+k|t}}{\mathbb{E}_t \sum_{k=0}^{\infty} \theta^k\, Q_{t,t+k}\, Y_{t+k|t}} \;} \tag{31}
$$

The optimal price is a markup $\mathcal{M}$ over a weighted average of expected nominal marginal costs over the life of the price. With flexible prices ($\theta = 0$) it reduces to $P_t^* = \mathcal{M}\,\psi_{t|t}$.

### Log-linearisation around the steady state

We divide (32) by $P_t$ and work with real marginal cost $MC_{t+k|t} = \psi_{t+k|t}/P_{t+k}$. In the zero-inflation steady state $P_t^* = P_t = P_{t+k}$, so:

$$
1 - \frac{\varepsilon}{\varepsilon-1}\, \overline{MC} = 0 \iff \overline{MC} = \frac{\varepsilon - 1}{\varepsilon} = \frac{1}{\mathcal{M}}
$$

Using lowercase letters for logs and $\widehat{mc}_{t+k} = mc_{t+k} - \overline{mc}$ for the deviation of real marginal cost, the first-order approximation of the bracketed term in (32) is:

$$
(p_t^* - p_t) - \left( \widehat{mc}_{t+k} + p_{t+k} - p_t \right) \tag{34}
$$

Condition (32) then becomes:

$$
\begin{aligned}
\sum_{k=0}^{\infty} (\theta\beta)^k\, \mathbb{E}_t \left[ (p_t^* - p_t) - (\widehat{mc}_{t+k} + p_{t+k} - p_t) \right] &= 0 \\
(p_t^* - p_t) \sum_{k=0}^{\infty} (\theta\beta)^k &= \sum_{k=0}^{\infty} (\theta\beta)^k\, \mathbb{E}_t \left[ \widehat{mc}_{t+k} + p_{t+k} - p_t \right] \\
\frac{p_t^* - p_t}{1 - \theta\beta} &= \sum_{k=0}^{\infty} (\theta\beta)^k\, \mathbb{E}_t \left[ \widehat{mc}_{t+k} + p_{t+k} - p_t \right]
\end{aligned}
\tag{35–38}
$$

$$
p_t^* - p_t = (1 - \theta\beta) \sum_{k=0}^{\infty} (\theta\beta)^k\, \mathbb{E}_t \left[ \widehat{mc}_{t+k} + p_{t+k} - p_t \right] \tag{39}
$$

In the steady state $Q_{t,t+k}Y_{t+k|t}$ is proportional to $\beta^k$, which is why the effective discount factor is $(\theta\beta)^k$.

### Calvo price dynamics

A fraction $1-\theta$ of firms set $p_t^*$ and the rest keep last period's price. In logs, the aggregate price level evolves as:

$$
p_t = \theta\, p_{t-1} + (1-\theta)\, p_t^*
$$

Subtracting $p_{t-1}$ from both sides, with $\pi_t = p_t - p_{t-1}$:

$$
\begin{aligned}
\pi_t &= (1-\theta)(p_t^* - p_{t-1}) \\
&= (1-\theta)\big[ (p_t^* - p_t) + (p_t - p_{t-1}) \big] \\
&= (1-\theta)(p_t^* - p_t) + (1-\theta)\pi_t
\end{aligned}
\tag{40–46}
$$

Therefore:

$$
\boxed{\; p_t^* - p_t = \frac{\theta}{1-\theta}\, \pi_t \;} \tag{47}
$$

The gap between the optimal price and the price level is expressed in terms of inflation and the degree of rigidity $\theta$.

### Removing the infinite sum

We write (39) recursively. Separating the $k=0$ term and re-indexing the rest:

$$
p_t^* - p_t = (1-\theta\beta)\, \widehat{mc}_t + \theta\beta\, \mathbb{E}_t\!\left[ p_{t+1}^* - p_t \right]
$$

The last term decomposes as $p_{t+1}^* - p_t = (p_{t+1}^* - p_{t+1}) + \pi_{t+1}$, so:

$$
p_t^* - p_t = (1-\theta\beta)\, \widehat{mc}_t + \theta\beta\, \mathbb{E}_t\!\left[ p_{t+1}^* - p_{t+1} \right] + \theta\beta\, \mathbb{E}_t[\pi_{t+1}] \tag{49–51}
$$

This is the same result obtained by leading (39) one period, multiplying it by $\theta\beta$ and subtracting it from the equation at $t$: almost every term in the sum cancels.

### The New Keynesian Phillips Curve

Substituting (47) at $t$ and at $t+1$:

$$
\begin{aligned}
\frac{\theta}{1-\theta}\pi_t &= (1-\theta\beta)\, \widehat{mc}_t + \theta\beta\, \frac{\theta}{1-\theta}\, \mathbb{E}_t[\pi_{t+1}] + \theta\beta\, \mathbb{E}_t[\pi_{t+1}] \\
&= (1-\theta\beta)\, \widehat{mc}_t + \theta\beta \left( \frac{\theta + 1 - \theta}{1-\theta} \right) \mathbb{E}_t[\pi_{t+1}] \\
&= (1-\theta\beta)\, \widehat{mc}_t + \frac{\theta\beta}{1-\theta}\, \mathbb{E}_t[\pi_{t+1}]
\end{aligned}
$$

Multiplying by $\dfrac{1-\theta}{\theta}$:

$$
\pi_t = \frac{(1-\theta)(1-\theta\beta)}{\theta}\, \widehat{mc}_t + \beta\, \mathbb{E}_t[\pi_{t+1}] \tag{52–53}
$$

Defining $\kappa \equiv \dfrac{(1-\theta)(1-\theta\beta)}{\theta}$, the slope that measures the sensitivity of inflation to real marginal cost:

$$
\boxed{\; \pi_t = \kappa\, \widehat{mc}_t + \beta\, \mathbb{E}_t[\pi_{t+1}] \;} \tag{54}
$$

Equation (54) is the **New Keynesian Phillips Curve**: current inflation depends on current real marginal cost and on expected future inflation. Iterating it forward, $\pi_t = \kappa \sum_{k=0}^{\infty} \beta^k\, \mathbb{E}_t[\widehat{mc}_{t+k}]$: inflation is the present value of future real marginal costs.

In Galí (2015) the slope also includes a factor $\Theta = \frac{1-\alpha}{1-\alpha+\alpha\varepsilon}$ when technology has decreasing returns; with constant returns ($\alpha = 0$) it matches the expression above.

## References

- Calvo, G. A. (1983). Staggered prices in a utility-maximizing framework. *Journal of Monetary Economics*, 12(3), 383–398.
- Galí, J. (2015). *Monetary Policy, Inflation, and the Business Cycle: An Introduction to the New Keynesian Framework* (2nd ed.). Princeton University Press.
