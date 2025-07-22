# k-means kümeleme kodu

# STEP 2
# k-means ile 3 kümeye ayıralım

from sklearn.cluster import KMeans

def cluster_coordinates(coordinates,n_clusters=3):
    model = KMeans(n_clusters=n_clusters,random_state=42)
    labels = model.fit_predict(coordinates)
    centroids = model.cluster_centers_
    return labels,centroids