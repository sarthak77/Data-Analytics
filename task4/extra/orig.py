import numpy as np
import matplotlib.pyplot as plt

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

#Apply PCA to reduce to 2-dimensions
T=train_data.T
C=np.cov(T)
E,V=np.linalg.eig(C)
E=E.real
V=V.real
X=[]
Y=[]
for i in range(6000):
    X.append(np.matmul(T[:,i].T,V[:,0]))
    Y.append(np.matmul(T[:,i].T,V[:,1]))
plt.scatter(X,Y,marker='*')
plt.show()

inp=[]
for i in range(6000):
    inp.append([X[i],Y[i]])

# print(inp)