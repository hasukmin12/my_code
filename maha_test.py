import numpy as np
from scipy.spatial.distance import cdist

x = np.array([[[1,2,3],
               [3,4,5],
               [5,6,7]],
              [[5,6,7],
               [7,8,9],
               [9,0,1]]])

i,j,k = x.shape

xx = x.reshape(i,j*k).T


y = np.array([[[8,7,6],
               [6,5,4],
               [4,3,2]],
              [[4,3,2],
               [2,1,0],
               [0,1,2]]])


yy = y.reshape(i,j*k).T

results =  cdist(xx,yy,'mahalanobis')

results = np.diag(results)
print (results)