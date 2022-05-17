
    
class Graph:
    #https://www.geeksforgeeks.org/strongly-connected-components/
    # init function to declare class variables
    def __init__(self):
        self.adj = {}
        self.V = []
 
    def DFSUtil(self, temp, v, visited):
 
        # Mark the current vertex as visited
        visited[v] = True
 
        # Store the vertex to list
        temp.append(v)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
 
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp
 
    # method to add an undirected edge
    def addEdge(self, v, w):
        if v in self.adj:
            self.adj[v].append(w)
        else:
            self.adj[v]= [w]
            self.V.append(v)
        if w in self.adj:
            self.adj[w].append(v)
        else:
            self.adj[w] = [v]
            self.V.append(w)
 
    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = {}
        cc = []
        for i in self.V:
            visited[i]=False
        for v in self.V:
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc
        
        