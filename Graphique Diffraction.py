import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import math

# Charger les données
file_path = "Double_0.04.csv"  # Remplace par le bon chemin de fichier
data = pd.read_csv(file_path, names=["Distance (cm)", "Gray Value"], header=None)

# Détection des pics avec un seuil d'intensité
peaks, _ = find_peaks(data["Gray Value"], height=50)  # Seuil ajustable si nécessaire

# Extraire les distances et valeurs des pics détectés
peak_distances = data["Distance (cm)"].iloc[peaks]
peak_values = data["Gray Value"].iloc[peaks]

# Sélectionner le maximum dans la plage 5.90 cm - 6.14 cm
first_peak_subset = peak_values[(peak_distances > 7.28) & (peak_distances < 7.35)]
first_peak_idx = first_peak_subset.idxmax()  # Prend l'indice du maximum d'intensité
first_peak_pos = data["Distance (cm)"].loc[first_peak_idx]
first_peak_value = data["Gray Value"].loc[first_peak_idx]

# Sélectionner le maximum dans la plage 6.86 cm - 7.32 cm
second_peak_subset = peak_values[(peak_distances > 7.41) & (peak_distances < 7.48)]
second_peak_idx = second_peak_subset.idxmax()  # Prend l'indice du maximum d'intensité
second_peak_pos = data["Distance (cm)"].loc[second_peak_idx]
second_peak_value = data["Gray Value"].loc[second_peak_idx]

# Sélectionner le maximum dans la plage 7.91 cm - 8.26 cm
third_peak_subset = peak_values[(peak_distances > 7.51) & (peak_distances < 7.59)]
third_peak_idx = third_peak_subset.idxmax()  # Prend l'indice du maximum d'intensité
third_peak_pos = data["Distance (cm)"].loc[third_peak_idx]
third_peak_value = data["Gray Value"].loc[third_peak_idx]

# Calculer la distance entre les deux pics
distance_between_peaks1 = abs(second_peak_pos - first_peak_pos)

distance_between_peaks2 = abs(third_peak_pos - second_peak_pos)

mean_between_peak = (distance_between_peaks1+distance_between_peaks2)/2

#Calculer a et d
m_n = 1
lambda_nm = 650e-9  # 650 nm en mètres

angle_radians = math.atan( 0.1233 / 40)

# Calcul de 'a' à partir de l'équation: a = (m_n * lambda) / sin(theta)
a = (m_n * lambda_nm) / math.sin(angle_radians)

print("Angle theta (en radians) :", angle_radians)
print("Largeur de la fente a (en mètres) :", a)

# Affichage des résultats
#print(f"Premier maximum (autour de 6 cm) : {first_peak_pos:.4f} cm, Intensité : {first_peak_value}")
#print(f"Deuxième maximum (autour de 7 cm) : {second_peak_pos:.4f} cm, Intensité : {second_peak_value}")
#print(f"Distance entre les deux : {distance_between_peaks1:.4f} cm")

#print(f"Deuxième maximum (autour de 7 cm) : {second_peak_pos:.4f} cm, Intensité : {second_peak_value}")
#print(f"Troisième maximum (autour de 8 cm) : {third_peak_pos:.4f} cm, Intensité : {third_peak_value}")
#print(f"Distance entre les deux : {distance_between_peaks2:.4f} cm")

#print(f"Moyenne des distances entre les maximas : {mean_between_peak:.4f} cm")


# Tracer le graphique avec les maxima en rouge
#plt.figure(figsize=(8, 5))
#plt.plot(data["Distance (cm)"], data["Gray Value"], label="Intensité")
#plt.scatter([first_peak_pos, second_peak_pos, third_peak_pos], 
            #[first_peak_value, second_peak_value, third_peak_value], 
            #color="red", label="Maxima sélectionnés")
#plt.xlabel("Distance (cm)")
#plt.ylabel("Gray Value")
#plt.title("Intensité avec maxima sélectionnés")
#plt.legend()
#plt.grid(False)
#plt.show()