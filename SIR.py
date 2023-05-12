import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def vac_model(t, y, tau, kappa, alpha):
    S, I, R, V = y
    dSdt = -tau*S*I - alpha*S*V
    dIdt = tau*S*I - I/kappa
    dRdt = I/kappa
    dVdt = alpha*S*V
    return [dSdt, dIdt, dRdt, dVdt]

y0 = [0.98, 0.01, 0, 0.01]
tau = 0.4
kappa = 8
alpha = 0.1

def stop_condition(t, y):
    return y[1] - 1e-4

stop_condition.terminal = True

t_start = 0
t_end = 200
t_span = (t_start, t_end)

sol = solve_ivp(fun=lambda t, y: vac_model(t, y, tau, kappa, alpha), t_span=t_span, y0=y0, events=stop_condition)

t = sol.t
y = sol.y


print(f"Stopping time: {sol.t[-1]:.2f} days")

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t, y[0], label='Susceptible')
ax.plot(t, y[1], label='Infected')
ax.plot(t, y[2], label='Recovered')
ax.plot(t, y[3], label='Vaccinated')
ax.set_xlabel('Time')
ax.set_ylabel('population')
ax.set_ylim(0, 1)
ax.legend()
plt.show()



