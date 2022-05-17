from collections import defaultdict


class Graph2:
    #https://www.geeksforgeeks.org/union-find/
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
  
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def removeEdge(self,u,v):
        self.graph[u].remove(v)
  
    # A utility function to find the subset of an element i
    def find_parent(self, parent,i):
        if parent[i] == -1:
            return i
        if parent[i]!= -1:
             return self.find_parent(parent,parent[i])
 
    # A utility function to do union of two subsets
    def union(self,parent,x,y):
        parent[x] = y
 
  
  
    # The main function to check whether a given graph
    # contains cycle or not
    def isCyclic(self):
         
        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = [-1]*(self.V)
 
        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent,x,y) 
        return False