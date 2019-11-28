import numpy as np
import matplotlib.pyplot as plt
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



#segregate data classwise
dig=[]
for i in range(10):
    t=train_data[train_labels==i]
    dig.append(t)

#create an array of colors
col=cm.rainbow(np.linspace(0,1,10))



#Find E and V of origianl data matrix
T=train_data.T
C=np.cov(T)
E,V=np.linalg.eig(C)
E=E.real
V=V.real

#Apply PCA to reduce to 2-dimensions
for x in range(10):
    T=dig[x].T
    X=[]
    Y=[]
    for i in range(600):
        X.append(np.matmul(T[:,i].T,V[:,0]))
        Y.append(np.matmul(T[:,i].T,V[:,1]))
    plt.scatter(X,Y,marker='*',color=col[x])
    plt.title(str(x))
    plt.show()

plt.show()