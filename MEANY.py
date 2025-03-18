import numpy as np
import matplotlib.pyplot as plt

# Charger les données depuis le fichier .npy
loaded_data = np.load('moyennes_par_10ms.npy', allow_pickle=True).item()

# Accéder aux données
loaded_binned_time = loaded_data['Time (s)']
loaded_binned_mean = loaded_data['Moyenne (V)']

# Tracer les données
plt.figure(figsize=(10, 6))
plt.plot(loaded_binned_time, loaded_binned_mean, label='Moyenne par intervalles de 10 ms', color='green')

# Ajouter des détails au graphique
plt.title('Moyenne des données par intervalles de 10 ms')
plt.xlabel('Temps (s)')
plt.ylabel('Voltage (V)')
plt.legend()

# Afficher le graphique
plt.show()