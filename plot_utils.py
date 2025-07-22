# grafik çizimi için fonksiyonlar (matplotlib)

# STEP3
# görselleştirme fonku

import matplotlib.pyplot as plt

def plot_clusters(coordinates,labels,centroids,title = "K-means Clustering"):
    plt.figure(figsize=(8,6))
    for i in range(3):
        cluster_points = coordinates[labels==1]
        plt.scatter(cluster_points[:,0],cluster_points[:,1],label=f"Cluster {i+1}")
    plt.scatter(centroids[:,0],centroids[:,1],color="black",marker='x',s=100,label= "Centroids") 
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()   
    

def plot_route(points, route, title="Route", save_path=None):
    route_points = points[route]
    plt.figure(figsize=(6, 6))
    plt.plot(route_points[:, 0], route_points[:, 1], marker='o')
    for i, point in enumerate(route_points):
        plt.text(point[0]+0.5, point[1]+0.5, str(i), fontsize=8)
    plt.title(title)
    plt.grid(True)
    if save_path:
        plt.savefig(save_path)
        print(f"✅ Grafik kaydedildi: {save_path}")
    plt.close()    