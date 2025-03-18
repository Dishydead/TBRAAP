import numpy as np
import matplotlib.pyplot as plt

# Load the structured array
data = np.load("5secsTube_1.npy")

# Extract fields from the structured array
time = data['Time (s)']
channel1 = data['Input 1 (V)']

# Définir le seuil
threshold = 0.325

# Filtrer les données au-dessus du seuil
filtered_values = channel1[channel1 > threshold]

# Calculer la moyenne et l'incertitude pour les données filtrées
mean_filtered = np.mean(filtered_values)
std_filtered = np.std(filtered_values)

# Afficher les résultats
print(f"Moyenne des données au-dessus de {threshold} V : {mean_filtered:.6f} V")
print(f"Incertitude des données filtrées : {std_filtered:.6f} V")

# Create the plot
plt.figure(figsize=(10, 6))  # Optional: sets the size of the plot

# Plot both channels with different colors
plt.plot(time, channel1, label='Bruit', color='blue')

# Add titles and labels
plt.title('Représentation du bruit (sans tube 5 secondes)')
plt.xlabel('Temps (s)')
plt.ylabel('Voltage (V)')
plt.legend()

plt.show()