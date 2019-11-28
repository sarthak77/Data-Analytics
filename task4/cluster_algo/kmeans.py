from pyclustering.cluster.kmeans import kmeans, kmeans_visualizer
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.samples.definitions import FCPS_SAMPLES,FAMOUS_SAMPLES
from pyclustering.utils import read_sample
# Load list of points for cluster analysis.
sample = read_sample(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS)
# sample = read_sample(FAMOUS_SAMPLES.SAMPLE_IRIS)
lines = open("t4.8k","r")
inp = []
for line in lines:
	cords = line.split()
	if len(cords) != 2:
		continue
	inp.append([float(cords[0]), float(cords[1])])
	
# Prepare initial centers using K-Means++ method.
# initial_centers = kmeans_plusplus_initializer(inp, 6).initialize()
initial_centers = kmeans_plusplus_initializer(sample,4).initialize()

# Create instance of K-Means algorithm with prepared centers.
# kmeans_instance = kmeans(inp, initial_centers)
kmeans_instance = kmeans(sample, initial_centers)

# Run cluster analysis and obtain results.
kmeans_instance.process()
clusters = kmeans_instance.get_clusters()
final_centers = kmeans_instance.get_centers()

# Visualize obtained results
# kmeans_visualizer.show_clusters(inp, clusters, final_centers)
kmeans_visualizer.show_clusters(sample, clusters, final_centers)