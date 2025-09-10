import numpy as np
import matplotlib.pyplot as plt

# Parameters
L0 = 100  # Initial BOD in mg/L
k = 0.35  # BOD rate constant in day^-1

# Time range: until BOD is ~5% remaining => solve t = -ln(0.05)/k
t_end = int(np.ceil(-np.log(0.05) / k)) + 1
t = np.linspace(0, t_end, 500)

# BOD remaining over time
L_t = L0 * np.exp(-k * t)

# Calculate time to reach specific percentages of BOD remaining
percent_remaining = np.array([0.75, 0.50, 0.25, 0.10, 0.05])
times = -np.log(percent_remaining) / k

# Table of results
print("Percent Remaining\tTime (days)")
for p, time_p in zip(percent_remaining, times):
    print(f"{int(p*100)}%\t\t\t{time_p:.2f}")

# Plotting
plt.figure(figsize=(10,6))
plt.plot(t, L_t, label=f'BOD Degradation (k = {k} day$^{{-1}}$)')
plt.title('BOD Degradation Over Time')
plt.xlabel('Time (days)')
plt.ylabel('BOD Remaining (mg/L)')
plt.grid(True)

# Mark points of interest
for p, tp in zip(percent_remaining, times):
    plt.axvline(tp, linestyle='--', color='gray', alpha=0.6)
    plt.scatter(tp, L0*p, color='red')
    plt.text(tp, L0*p + 2, f'{int(p*100)}% BOD\n{tp:.1f} days', ha='center', fontsize=9)

plt.legend()
plt.tight_layout()
plt.show()
