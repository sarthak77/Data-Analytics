import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import matplotlib.cm as cm

def read_data(filename):
    """
    Returns data and labels from the dataset
    """

    with open(filename, 'r') as f:
        lines = f.readlines()
    
    num_points = len(lines)
    dim_points = 28 * 28
    data = np.empty((num_points, dim_points))
    labels = np.empty(num_points)
    
    for ind, line in enumerate(lines):
        num = line.split(',')
        labels[ind] = int(num[0])
        data[ind] = [ int(x) for x in num[1:] ]
        
    return (data, labels)

train_data, train_labels = read_data("mnist.csv")
# print(train_data.shape)
# print(train_labels.shape)
    
X = TSNE(n_components=2).fit_transform(train_data)

x=X[:,0]
y=X[:,1]

#segregate data classwise
dig=[]
for i in range(10):
    t=X[train_labels==i]
    dig.append(t)

#create an array of colors
col=cm.rainbow(np.linspace(0,1,10))

for i in range(10):
    print(i)
    for j in dig[i]:
        # print(j)
        plt.scatter(j[0],j[1],color=col[0])

# plt.scatter(x,y)
plt.show()