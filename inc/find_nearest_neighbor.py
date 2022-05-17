from inc.ED import ED
from collections import namedtuple


NearestNeighbor = namedtuple("NearestNeighbor", ["point", "distance"])

def find_nearest_neighbor(*, tree, point):
    #https://johnlekberg.com/blog/2020-04-17-kd-tree.html
    
    bestP = None
    bestV = None
    def search(*, tree, depth):
        #Recursively search through the k-d tree to find the nearest neighbor.
        nonlocal bestP
        nonlocal bestV
        
        if tree is None:
            return
        
        distance = ED(tree.value, point)
        if bestV is None or distance < bestV:
            bestP = tree.value
            bestV = distance
        
        axis = depth % 2
        diff = point[axis] - tree.value[axis]
        if diff <= 0:
            close, away = tree.left, tree.right
        else:
            close, away = tree.right, tree.left
        
        search(tree=close, depth=depth+1)
        if diff < bestV:
            search(tree=away, depth=depth+1)
    
    search(tree=tree, depth=0)
    return NearestNeighbor(bestP, bestV)