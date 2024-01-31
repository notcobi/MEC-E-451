import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
df = pd.read_csv('Lab 1\matplotlib\data.csv')

# Import the x, y, z acceleration data
t = df['time']
x = df['x acceleration']
y = df['y acceleration']
z = df['z acceleration']

# Plot the data, first 50 points
plt.plot(t[:50], z[:50], '-o', label='x acceleration', markersize=6, markerfacecolor='none')

# Find the first 2 peaks
peak1 = np.argmax(z[:15])
peak2 = np.argmax(z[22:30]) + 22

# Set the title and labels
plt.xlabel(r'$t$, Time (s)')
plt.ylabel(r'$a_{z}$, z Acceleration (m/s$^{2}$)')

# Annotate the peaks
plt.annotate("(" + str(z[peak1]) + ", " + str(t[peak1]) + ")", xy=(t[peak1], z[peak1]), xytext=(t[peak1] +0.05, z[peak1] + 0.05), arrowprops=dict(facecolor='black', shrink=0.03, width=0.5, headwidth=4, headlength=3))

plt.annotate("(" + str(z[peak2]) + ", " + str(t[peak2]) + ")", xy=(t[peak2], z[peak2]), xytext=(t[peak2] +0.05, z[peak2]), arrowprops=dict(facecolor='black', shrink=0.03, width=0.5, headwidth=4, headlength=3))

# Save the plots
plt.savefig('Lab 1\Questions\Plots\z_acceleration.png', dpi=300)



# # Plot the data
# plt.plot(df_micrometer['n'], df_micrometer['P'], '-o', label='Micrometer', markersize=6, markerfacecolor='none')
# plt.plot(df_vernier['n'], df_vernier['P'], '-s', label='Vernier Caliper', markersize=6, markerfacecolor='none')
# plt.plot(df_digital['n'], df_digital['P'], '-^', label='Digital Caliper', markersize=6, markerfacecolor='none')


# # Set the title and labels
# plt.xlabel(r'$n$, Number of Measurements')
# plt.ylabel(r'$P_{x}$, Precision (mm)')
# plt.legend()

# # Set x-axis ticks to integer values with tick mark rotation
# plt.xticks(np.arange(df['n'].min(), df['n'].max()+1, 1), rotation=45, ha = 'left')

# # Save the plots
# plt.savefig('Q3_Precision.png', dpi=300)

# # Make new plot
# plt.figure()
# plt.plot(df_micrometer['n'], df_micrometer['U'], '-o', label='Micrometer', markersize=6, markerfacecolor='none')
# plt.plot(df_vernier['n'], df_vernier['U'], '-s', label='Vernier Caliper', markersize=6, markerfacecolor='none')
# plt.plot(df_digital['n'], df_digital['U'], '-^', label='Digital Caliper', markersize=6, markerfacecolor='none')

# # Set the title and labels
# plt.xlabel(r'$n$, Number of Measurements')
# plt.ylabel(r'$U_{x}$, Uncertainty (mm)')
# plt.legend()

# # Set x-axis ticks to integer values with tick mark rotation
# plt.xticks(np.arange(df['n'].min(), df['n'].max()+1, 1), rotation=45, ha = 'left')

# # Save the plots
# plt.savefig('Q3_Uncertainty.png', dpi=300)

# # Show the plot
# plt.show()


