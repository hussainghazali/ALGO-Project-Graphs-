# Python program for Bellman-Ford's single source 
# shortest path algorithm.
 
from collections import defaultdict
 
  

 
#Class to represent a graph
class Graph_bellman:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u, v, w])
         
    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))
     
    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm.  The function
    # also detects negative weight cycle
    def BellmanFord(self, src):
 
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        li=range(self.V)
        previous = dict.fromkeys(li, None)
        dist[int(src)] = 0
 
 
        # Step 2: Relax all edges |V| - 1 times. A simple shortest 
        # path from src to any other vertex can have at-most |V| - 1 
        # edges
        for i in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        previous[v]=u
 
        # Step 3: check for negative-weight cycles.  The above step 
        # guarantees shortest distances if graph doesn't contain 
        # negative weight cycle.  If we get a shorter path, then there
        # is a cycle.
 
        for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        #print "Graph contains negative weight cycle"
                        return -1,-1
                         
        # print all distance
        return dist,previous


    def shortest_path(self,g, start, end):
      delta, previous = g.BellmanFord(start)
      
      if delta==-1 and previous==-1:
        return -1
      path = []
      vertex = int(end)

      while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]

      path.reverse()
      return path
 
'''g = Graph(4)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
g.addEdge(0, 1, 5)
g.addEdge(1, 0, 3)
g.addEdge(3, 0, -1)
g.addEdge(1, 3, 4)
g.addEdge(2, 3, 6)
g.addEdge(0, 2, 2)

 
#Print the solution
dist,prev=g.BellmanFord(0)
print prev,dist

path=g.shortest_path(g, 0, 3)
if path==-1:
    print "negative cycle detects"
else:
    print path
 '''