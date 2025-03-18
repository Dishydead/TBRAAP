import matplotlib.pyplot as plt

# Données
categories = ["Monomode", "Multimode Low", "Multimode High", "Itensité du Laser"]
values = [410, 522, 553, 650]

# Création du diagramme à bandes
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=['blue', 'orange', 'green', "red"])

# Ajout des labels et du titre
plt.ylabel("Courant (\u03BCA)")  # \u03BC est le code Unicode pour le symbole mu

# Ajustement de la précision de l'axe y
plt.yticks(range(0, max(values) + 30, 70))
# Affichage du graphique
plt.show()
