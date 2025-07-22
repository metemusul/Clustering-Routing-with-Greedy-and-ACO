# STEP 4

from data import generate_coordinates
from clustering import cluster_coordinates
from plot_utils import plot_clusters, plot_route
from routing import greedy_tsp
from aco import AntColony
import matplotlib.pyplot as plt
import numpy as np
import os

# Veri üretimi ve kümeleme
coordinates = generate_coordinates()
labels, centroids = cluster_coordinates(coordinates)
plot_clusters(coordinates, labels, centroids)

# 📁 Greedy çıktı klasörü
greedy_dir = "greedy_cikti"
os.makedirs(greedy_dir, exist_ok=True)

# Greedy TSP rotaları ve çizimleri
for i in range(3):
    cluster_points = coordinates[labels == i]
    if len(cluster_points) < 2:
        continue

    route = greedy_tsp(cluster_points)
    save_file = os.path.join(greedy_dir, f"cluster_{i+1}_greedy.png")
    plot_route(cluster_points, route, title=f"Cluster {i+1} Greedy", save_path=save_file)

# 📁 ACO çıktı klasörü
aco_dir = "aco_cikti"
os.makedirs(aco_dir, exist_ok=True)

# ACO algoritması uygulaması
for i in range(3):
    cluster_points = coordinates[labels == i]
    if len(cluster_points) < 2:
        continue

    n = len(cluster_points)
    distance_matrix = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            if a != b:
                distance_matrix[a][b] = np.linalg.norm(cluster_points[a] - cluster_points[b])
            else:
                distance_matrix[a][b] = np.inf  # Kendine mesafe ∞

    colony = AntColony(
        distances=distance_matrix,
        n_ants=20,
        n_best=5,
        n_iterations=100,
        decay=0.05,
        alpha=1,
        beta=2
    )

    best_path, best_dist = colony.run()

    # Rota çizimi
    route = best_path + [best_path[0]]  # Başladığı yere dön
    save_file = os.path.join(aco_dir, f"cluster_{i+1}_aco.png")
    plot_route(cluster_points, route, title=f"Cluster {i+1} ACO (dist={best_dist:.2f})", save_path=save_file)
