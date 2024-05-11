
from sklearn.cluster import MiniBatchKMeans
import numpy as np

def agrupar_datos(datos, n_clusters):
    """
    Agrupa datos utilizando MiniBatchKMeans.

    Parámetros:
    - datos: Un array numpy que contiene los datos a agrupar.
    - n_clusters: El número de clústeres que se desea encontrar.

    Retorna:
    - etiquetas: Las etiquetas de clúster asignadas a cada muestra.
    - centroides: Las coordenadas de los centroides de los clústeres encontrados.
    """

    # Crear una instancia de MiniBatchKMeans
    kmeans = MiniBatchKMeans(n_clusters=n_clusters)

    # Ajustar el modelo a los datos
    kmeans.fit(datos)

    # Obtener las etiquetas de los clústeres para cada muestra
    etiquetas = kmeans.labels_

    # Obtener las coordenadas de los centroides de los clústeres
    centroides = kmeans.cluster_centers_

    return etiquetas, centroides


# Generar datos de ejemplo
np.random.seed(0)  # Fijar la semilla para reproducibilidad
n_muestras = 1000
n_caracteristicas = 2
datos = np.random.randn(n_muestras, n_caracteristicas)

# Llamar a la función de agrupamiento
etiquetas, centroides = agrupar_datos(datos, n_clusters=5)

# Imprimir las etiquetas de los clústeres y las coordenadas de los centroides
print("Etiquetas de los clústeres:")
print(etiquetas)
print("\nCoordenadas de los centroides:")
print(centroides)