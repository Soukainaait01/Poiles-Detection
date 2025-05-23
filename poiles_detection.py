

#image_path = "C:/Users/user/Downloads/image1.jpeg"  # 
import cv2
import numpy as np
import matplotlib.pyplot as plt

# === 1. Charger l'image ===
image_path = "C:/Users/user/Downloads/image1.jpeg"   # Remplace ceci
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# === 2. Réduction du bruit ===
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# === 3. Détection des contours (Canny) ===
edges = cv2.Canny(blurred, 30, 100)

# === 4. Contours potentiels de poils ===
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
min_length = 10  # Ajuste selon les images
filtered_contours = [cnt for cnt in contours if cv2.arcLength(cnt, False) > min_length]

# === 5. Dessiner les contours sur une copie ===
output = image.copy()
cv2.drawContours(output, filtered_contours, -1, (0, 255, 0), 1)

# === 6. Écrire le nombre de poils sur l'image ===
count = len(filtered_contours)
text = f"Nombre de poils : {count}"
cv2.putText(output, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# === 7. Afficher l’image originale + résultat côte à côte ===
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Image originale")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Poils détectés et comptés")
plt.axis('off')

plt.tight_layout()
plt.show()
