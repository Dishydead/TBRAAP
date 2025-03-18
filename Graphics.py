import numpy as np
import matplotlib.pyplot as plt

# Load the structured array
data = np.load("5secsTube_1.npy")

# Extract fields from the structured array
time = data['Time (s)']
channel1 = data['Input 1 (V)']

# Create the plot
plt.figure(figsize=(10, 6))  # Optional: sets the size of the plot

# Plot both channels with different colors
plt.plot(time, channel1, label='Signal', color='blue')

# Add titles and labels
#plt.title('Représentation du signal bruit (avec tube 5 secondes)')
plt.xlabel('Temps (s)')
plt.ylabel('Voltage (V)')
plt.legend()

# Show the plot
plt.show()