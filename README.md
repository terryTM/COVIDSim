# COVIDSim
**SIR Model simulation of disease spread**

We can assume the behavior of a disease is governed by the following mathematical model. Denote time by a continuous variable $t \geq 0$, and let the state of the system be represented by the three dimensional vector,

$$x = [S(t), I(t), R(t)]$$

where $S(t), I(t), and R(t)$ denote the fractions of the population who are susceptible, infected, or recovered, respectively, at time $t$.

We assume $x$ evolves as an ordinary differential equation,

$$Dx = f(x)$$

where $f(x)$ is the vector function,

$$f(x) = [-\tau S(t) I(t), -\tau S(t) I(t) - \frac{I(t)}{\kappa}, \frac{I(t)}{\kappa}]$$

The parameter $\tau \geq 0$ measures how quickly the disease can spread, with higher values corresponding to faster rates of spread. The parameter $\kappa > 0$ measures how quickly an infected person recovers, with higher values corresponding to slower (longer) recovery times.
