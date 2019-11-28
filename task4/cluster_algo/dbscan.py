from pyclustering.cluster.dbscan import dbscan
from pyclustering.cluster import cluster_visualizer_multidim,cluster_visualizer
from pyclustering.utils import read_sample
from pyclustering.samples.definitions import FCPS_SAMPLES, FAMOUS_SAMPLES

# Sample for cluster analysis.
# sample = read_sample(FCPS_SAMPLES.SAMPLE_CHAINLINK)
sample = read_sample(FAMOUS_SAMPLES.SAMPLE_IRIS)
lines = open("t4.8k","r")
inp = []
for line in lines:
	cords = line.split()
	if len(cords) != 2:
		continue
	inp.append([float(cords[0]), float(cords[1])])
# print(inp)

# Create DBSCAN algorithm.
dbscan_instance = dbscan(inp, 5, 3)
# dbscan_instance = dbscan(sample, 5, 3)

# Start processing by DBSCAN.
dbscan_instance.process()

# Obtain results of clustering.
clusters = dbscan_instance.get_clusters()
# noise = dbscan_instance.get_noise()

# Visualize clustering results
visualizer = cluster_visualizer_multidim()
# visualizer = cluster_visualizer()
visualizer.append_clusters(clusters, inp, marker='o')
# visualizer.append_clusters(clusters, sample, marker='o')
# visualizer.append_cluster(noise, inp, marker='x')
visualizer.show()
