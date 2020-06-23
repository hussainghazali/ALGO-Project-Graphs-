import numpy as np
  

class floyd(object):
    """docstring for ClassName"""
    def __init__(self, graph):
        self.graph=graph
        self.final=[]
        self.v = len(graph)

        #self.p = np.zeros(self.graph.shape)
        

    def ConstructPath( self,i, j):
        p=self.ans()
        i,j = int(i), int(j)
        if(i==j):
          print (i,)
          self.final.append(i)
        elif(p[i,j] == -30000000):
          print (i,'-',j)
        else:
          self.ConstructPath(i, p[i,j]);
          self.final.append(j)
          print(j,)
        return self.final



    def ans(self):
    # path reconstruction matrix
        p = np.zeros(self.graph.shape)
        for i in range(0,self.v):
            for j in range(0,self.v):
                p[i,j] = i
                if (i != j and self.graph[i,j] == 0): 
                    p[i,j] = -30000000
                    self.graph[i,j] = 30000000  # set zeros to any large number which is bigger then the longest way

        for k in range(0,self.v):
            for i in range(0,self.v):
                for j in range(0,self.v):
                    if self.graph[i,j] > self.graph[i,k] + self.graph[k,j]:
                        self.graph[i,j] = self.graph[i,k] + self.graph[k,j]
                        p[i,j] = p[k,j]


        return p;

'''graph = np.array([[0,5,0,10],
             [0,0,3,0],
             [0, 0, 0,   1],
             [0, 0, 0, 0]
        ] )

g=floyd(graph)
hh=g.ConstructPath(0,2)
print(hh)'''               
# show p matrix

#print(p)

# reconstruct the path from 0 to 4
#ConstructPath(p,2,0)
#print(final)