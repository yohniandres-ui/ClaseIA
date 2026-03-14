import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

image = cv2.imread('CarsClassic.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
image = cv2.resize(image, (100, 100))
pixels = image.reshape((-1, 3)) 

k = 5  
kmeans = KMeans(n_clusters=k).fit(pixels)
colors = kmeans.cluster_centers_.astype(int)
plt.figure(figsize=(4, 2))
for i, color in enumerate(colors):
    plt.subplot(1, k, i + 1)
    plt.imshow([[color / 255]])
    plt.axis('off')
    plt.title(color, fontdict = {'fontsize': 8})
    print(f'RGB: ',color,'\n')
plt.tight_layout()
plt.show()
