import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Définir la grille de temps commune (par exemple, 0 à 5 secondes avec un pas de 1 ms)
time_common = np.arange(0, 5, 0.001)  # De 0 à 5 s avec un pas de 1 ms

# Nombre de fichiers et base des noms
num_files = 5
base_filename = "5secsTube_"

# Liste pour stocker les données interpolées
interpolated_data = []

# Charger chaque fichier, interpoler et stocker les données
for i in range(1, num_files + 1):
    filename = f"{base_filename}{i}.npy"  # Nom du fichier
    data = np.load(filename)
    
    # Extraire le temps et les données
    time = data['Time (s)']
    channel1 = data['Input 1 (V)']
    
    # Interpoler sur la grille de temps commune
    interpolation_func = interp1d(time, channel1, kind='linear', fill_value="extrapolate")
    interpolated_channel = interpolation_func(time_common)
    
    # Ajouter les données interpolées à la liste
    interpolated_data.append(interpolated_channel)

# Convertir en tableau NumPy
interpolated_data = np.array(interpolated_data)  # Shape: (num_files, len(time_common))

# Calculer la moyenne sur tous les fichiers
mean_data = np.mean(interpolated_data, axis=0)

# Regrouper les données par intervalles de 10 ms
bin_size = 0.01  # Taille des intervalles (10 ms)
bins = np.arange(0, 5 + bin_size, bin_size)  # Définir les bords des intervalles
digitized = np.digitize(time_common, bins)  # Associer chaque point de temps à un intervalle

# Calculer les moyennes pour chaque intervalle
binned_time = []
binned_mean = []

for i in range(1, len(bins)):
    indices = np.where(digitized == i)[0]  # Indices des points appartenant à l'intervalle
    if len(indices) > 0:
        binned_time.append(np.mean(time_common[indices]))  # Temps moyen de l'intervalle
        binned_mean.append(np.mean(mean_data[indices]))    # Moyenne des données dans l'intervalle

# Convertir en tableaux NumPy
binned_time = np.array(binned_time)
binned_mean = np.array(binned_mean)

# Tracer les données binned
plt.figure(figsize=(10, 6))
plt.plot(binned_time, binned_mean, label='Moyenne par intervalles de 10 ms', color='green')

# Ajouter des détails au graphique
plt.title('Moyenne des données par intervalles de 10 ms')
plt.xlabel('Temps (s)')
plt.ylabel('Voltage (V)')
plt.legend()

# Afficher le graphique
plt.show()
# Afficher les valeurs de chaque tranche de 10 ms
for time_val, mean_val in zip(binned_time, binned_mean):
    print(f"Temps: {time_val:.3f} s, Moyenne: {mean_val:.3f} V")

# Créer un dictionnaire avec les données à exporter
data_to_export = {
    'Time (s)': binned_time,
    'Moyenne (V)': binned_mean
}

# Sauvegarder dans un fichier .npy
np.save('moyennes_par_10ms.npy', data_to_export)

