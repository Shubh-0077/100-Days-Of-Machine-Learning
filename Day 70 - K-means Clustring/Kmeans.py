import numpy as np 
import random 

class Kmeans: 
    def __init__(self,n_clusters=2,max_iter=100): 
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None 

    def fit_predict(self,x): 
        random_index = random.sample(range(x.shape[0]),self.n_clusters)
        self.centroids = x[random_index]

        for _ in range(self.max_iter):
            # assign clusters to the nearest centroid
            cluster_groups = self.assign_clusters(x)
            new_centroids = self.move_clusters(x,cluster_groups)

            # move centroids to the mean of the assigned points 
            self.centroids = self.move_clusters(x,cluster_groups)
            # check finish
            if (old_centroids == self.centroids).all():
                break

        return cluster_groups

    def assign_clusters(self,x):   # random assigning 
        cluster_groups = []
        distances = []

        for row in x:
            for centroid in self.centroids:
                distances.append(np.sqrt(np.dot(row-centroid,row-centroid)))
            min_distance = min(distances)
            index_pos = distances.index(min_distance)
            cluster_groups.append(index_pos)
            distances.clear()

        return cluster_groups

    def move_clusters(self,x,cluster_groups):  # move clusters to the mean of the assigned points
        new_centroids = []

        cluster_type = np.unique(cluster_groups)

        for type in cluster_type:
            new_centroids.append(x[cluster_groups == type].mean(axis=0))

        return np.array(new_centroids)



