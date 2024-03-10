import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
df = pd.read_excel("Lab 2\matplotlib\Data from phyphox_part1.xlsx", sheet_name="analysis")

# Import the z acceleration data
df_omega_p = df["\omega/p"]
df_X = df['Displacement Amplitude (m)']

# Plot the data
plt.plot(df_omega_p, df_X, '-o', markersize=6, markerfacecolor='none')

# Set the title and labels
plt.xlabel(r'$\omega/p$')
plt.ylabel(r'$X$')

# Save the plots
plt.savefig(r'Lab 2\Questions\Plots\X_vs_omega_p.png', dpi=300, bbox_inches = "tight")

# Add a horizontal line at X = X_max/sqrt(2)
X_max = max(df_X)
plt.axhline(y=X_max/np.sqrt(2), color='r', linestyle='--', label=r'$X_{max}/\sqrt{2}$')

# Add a vertical line at omega/p = 1
plt.axvline(x=1, color='r', linestyle='--')

# Save the plots
plt.savefig(r'Lab 2\Questions\Plots\X_vs_omega_p_with_lines.png', dpi=300, bbox_inches = "tight")
