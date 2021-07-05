# Note that in the plot, the squares are the centroids from the standard k_means algorithm while the stars are the centroids from the mini-batch version of k_means.
from sklearn.cluster import MiniBatchKMeans, KMeans
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris 

data = load_iris() 
print ("Features :%s" % data.feature_names) 
features = data.data 
labels = data.target 

k_means = KMeans(n_clusters=3, init='k-means++',                  max_iter=999, n_init=1, random_state=101)

mb_k_means = MiniBatchKMeans(n_clusters=3, init='k-means++',         max_iter=999, batch_size=10, n_init=1, random_state=101)

k_means.fit(features) 
mb_k_means.fit(features)

plt.scatter(features[:,0], features[:,1], s=2**7, c=labels,             edgecolors='white', alpha=0.85, cmap='autumn') 
plt.grid() # adds a grid 
plt.xlabel(data.feature_names[0]) # adds label to x axis
plt.ylabel(data.feature_names[1]) # adds label to y axis

# Printing centroids, first of regular K-means, then of mini-batch
plt.scatter(k_means.cluster_centers_[:,0], k_means.cluster_centers_[:,1],             s=2**6, marker='s', c='blue') 
plt.scatter(mb_k_means.cluster_centers_[:,0], mb_k_means.cluster_centers_[:,1], s=2**8, marker='*', c='green')

for class_no in range(0,3): # We just annotate a point for each class     
    plt.annotate(data.target_names[class_no], (features[3+50*class_no,0],features[3+50*class_no,1])) 

plt.show() # Showing the result

# Enter k_means.cluster_centers at the command line to see the cooridinates of the cluster centers                  