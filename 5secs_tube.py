import numpy as np
import matplotlib.pyplot as plt

def find_start_index(signal, reference_value, tolerance=0.01):
    """
    Find the first index where the signal is close to the reference value.
    """
    for idx, value in enumerate(signal):
        if abs(value - reference_value) <= tolerance:
            return idx
    return 0  # Default to the start if no match is found

def align_signals_by_value(time, signals, reference_value, tolerance=0.01):
    """
    Align signals by trimming them to start at the first occurrence of a reference value.
    """
    aligned_time = []
    aligned_signals = []

    for t, s in zip(time, signals):
        # Find the starting index based on the reference value
        start_idx = find_start_index(s, reference_value, tolerance)
        
        # Trim the signal and time to start at the identified index
        aligned_time.append(t[start_idx:] - t[start_idx])
        aligned_signals.append(s[start_idx:])

    return aligned_time, aligned_signals

def adjust_to_shortest_length(aligned_time, aligned_signals):
    """
    Adjust all signals and time arrays to the shortest length.
    """
    # Find the shortest signal length
    min_length = min(len(s) for s in aligned_signals)
    
    # Truncate all signals and times to the minimum length
    adjusted_signals = [s[:min_length] for s in aligned_signals]
    adjusted_time = [t[:min_length] for t in aligned_time]
    
    return adjusted_time, adjusted_signals

# Load all files
file_paths = ["5secsTube_1.npy", "5secsTube_2.npy", "5secsTube_3.npy", "5secsTube_4.npy", "5secsTube_5.npy",
              "5secsTube_6.npy", "5secsTube_7.npy", "5secsTube_8.npy", "5secsTube_9.npy", "5secsTube_10.npy"]

time = []
signals = []

for path in file_paths:
    data = np.load(path, allow_pickle=True)
    time.append(data['Time (s)'])
    signals.append(data['Input 1 (V)'])

# Define a reference value (e.g., the starting value of the first file)
reference_value = signals[0][0]  # Use the initial value of the first file
tolerance = 0.01  # Adjust as needed for signal variability

# Align signals based on the reference value
aligned_time, aligned_signals = align_signals_by_value(time, signals, reference_value, tolerance)

# Adjust all aligned signals to the shortest length
adjusted_time, adjusted_signals = adjust_to_shortest_length(aligned_time, aligned_signals)

# Calculate the average of the adjusted signals
average_signal = np.mean(adjusted_signals, axis=0)

# Plot the average signal
plt.figure(figsize=(12, 6))
plt.plot(adjusted_time[0], average_signal, label="Average Aligned Signal", color="orange", linewidth=2)

# Plot individual aligned signals for comparison
for t, s in zip(adjusted_time, adjusted_signals):
    plt.plot(t, s, color="blue", alpha=0.3, linewidth=0.8)

# Add labels, title, and legend
plt.title("Signals Aligned and Adjusted by Reference Value")
plt.xlabel("Time (s)")
plt.ylabel("Signal Amplitude (V)")
plt.legend(["Average Signal", "Individual Signals"], loc="upper right")
plt.grid()
plt.show()