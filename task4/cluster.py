from pyclustering.cluster.dbscan import dbscan
from pyclustering.cluster import cluster_visualizer

#read inputs
lines = open("red_data.txt","r")
inp = []
for line in lines:
    line=line.strip()
    line=line[1:]
    line=line[:-1]
    line=line.split()
    inp.append([float(line[0]),float(line[1])])

# Create DBSCAN algorithm.
dbscan_instance = dbscan(inp,2.93,11)

# Start processing by DBSCAN.
dbscan_instance.process()

# Obtain results of clustering.
clusters = dbscan_instance.get_clusters()
noise = dbscan_instance.get_noise()

# Visualize clustering results
visualizer = cluster_visualizer()
visualizer.append_clusters(clusters, inp, marker='o')
visualizer.append_cluster(noise, inp, marker='x')
visualizer.show()