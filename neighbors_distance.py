from sklearn.neighbors import KDTree
from numpy import array

def neighbors_distance(X, *args, **kwargs):
    size = len(X)
    output = [[]] * size
    
    for i in range(len(X)):
        niegh_number = size

        X_tmp = [0]
        X_tmp.extend(X)
        X_tmp[0] = X[i]
        del X_tmp[i + 1]
        tree = KDTree(X_tmp, leaf_size=2)                     
        dist, ind = tree.query(X_tmp[:1], k=niegh_number)  
        res = [len(X)] * len(X) 
        pos = 0 
        for index in ind[0]:
            if pos == 0:
                res[i] = 0
            elif index <= i:
                res[index - 1] = pos
            else:
                res[index] = pos
            pos += 1
        output[i] = res 
    return array(output)