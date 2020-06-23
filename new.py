from __future__ import print_function

import pymysql

import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets


import dijsktra 
from dijsktra import Graph
import floyd 
from floyd import floyd
import kruskals 
from kruskals import Graph_kruk
import prims 
from prims import Graph_prim
import bellman 
from bellman import Graph_bellman

import networkx as nx
import matplotlib.pyplot as plot
import  numpy as np
import collections
import math     




qtCreatorFile = "algopro.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.workpage.setGeometry(QtCore.QRect(0,0,741,521))
        self.upload.clicked.connect(self.up)
        #filename,garbage_value_returning_ignore_it=QtWidgets.QFileDialog.getOpenFileName(self,'open a text file')
    def up(self):
                self.makegph.clicked.connect(self.doit)
                global file
                file=None
                filename,garbage_value_returning_ignore_it=QtWidgets.QFileDialog.getOpenFileName(self,'open a text file')
                file=open(filename,"r")
                file.readline()
                file.readline()
                global node
                node=int(file.readline())
                global matrix
                matrix=np.full((node,node),0.0)
                global x_axis
                x_axis=np.zeros((node))
                global y_axis
                y_axis=np.zeros((node))
                file.readline()

                for i in range(node):
                    line=file.readline().split()
                    n=int(line[0])
                    x_axis[n]=float(line[1])
                    y_axis[n]=float(line[2])
                    


                s2=[]
                file.readline()

                weight=file.readline().split()
                ind1=0
                ind2=1
                while(len(weight)!=0):
                    start=int(weight[ind1])
                    #print(start)
                    ind1=1
                    while(len(weight)>ind1):
                        
                        end=int(weight[ind1])
                        #print("end")
                        #print(end)
                        w=float(weight[ind1+2])
                        matrix[start][end]=w/10000000
                        ind1=ind1+4
                    
                        
                    ind1=0
                    weight=file.readline().split()

                start_node=int(file.readline())

    def doit(self):
        makegraph(self) 


def makegraph(self):
    choice=0
    choice=self.algo.currentIndex()
    s=int(self.st.text())
    e=int(self.en.text())
    
    #print(choice)
    if choice== 1:
        dij(self,matrix,node,s,e,x_axis,y_axis)
            

    if choice== 2:
        bellman(self,matrix,node,s,e,x_axis,y_axis)
            

    if choice== 3:
            
        prim(node,matrix,x_axis,y_axis)
                   
    if choice== 4:
            
        kruskal(node,matrix,x_axis,y_axis)

    if choice== 5:
        floyd1(self,matrix,node,s,e,x_axis,y_axis)   

    if choice==6:
        original_graph(node,matrix,x_axis,y_axis)




def floyd1(matrix,node,start_node,end_node,x_axis,y_axis):
    g=floyd(matrix)
    pp=g.ConstructPath( start_node,end_node)

    if pp==-1:
        self.output.setText("negative cycle detected")

    if len(pp)==1:
        self.output.setText ("it isn't connected with any node")
        return

    else:
        G=nx.DiGraph()

        for i in range(node):
             G.add_node(i,pos=(x_axis[i],y_axis[i]))

        for i in range(len(pp)-1):
            G.add_edge(pp[i],pp[i+1],weight=matrix[pp[i]][pp[i+1]])

        pos=nx.get_node_attributes(G,'pos')
        nx.draw(G,pos)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')



        plot.show() 






def bellman(self,matrix,node,start_node,end_node,x_axis,y_axis):
    g=Graph_bellman(node)
    for i in range(node):
        for j in range(node):
            if matrix[i][j]!=0:
                    g.addEdge(i, j, matrix[i][j])



    pp=g.shortest_path(g,start_node, end_node)
   # print(len(pp))  
    if pp==-1:
        self.output.setText ("negative cycle detects")

    if len(pp)==1:
        self.output.setText ("it doesnot connected with any node sorry :)")
        return

    else:
        G=nx.DiGraph()

        for i in range(node):
             G.add_node(i,pos=(x_axis[i],y_axis[i]))

        for i in range(len(pp)-1):
            G.add_edge(pp[i],pp[i+1],weight=matrix[pp[i]][pp[i+1]])

        pos=nx.get_node_attributes(G,'pos')
        nx.draw(G,pos)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')



        plot.show() 
                


def kruskal(node,matrix,x_axis,y_axis):
    g=Graph_kruk(node)
    for i in range(node):
        for j in range(node):
            if matrix[i][j]!=0:
                    g.addEdge(i, j, matrix[i][j])


    
    p=g.KruskalMST()                     





    G=nx.DiGraph()
    for i in range(node):
         G.add_node(i,pos=(x_axis[i],y_axis[i]))

    for u,v,weights in p:
        G.add_edge(u,v,weight=weights)

    pos=nx.get_node_attributes(G,'pos')
    nx.draw(G,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')



    plot.show()     




def prim(node,matrix,x_axis,y_axis):
    graph = Graph_prim(node)
    for i in range(node):
        for j in range(node):
            if matrix[i][j]!=0:
                graph.addEdge(i, j, matrix[i][j])




    p=graph.PrimMST()
    #for i in range(1,node):
    #    print "%d - %d" % (p[i], i)


    G=nx.DiGraph()
    for i in range(node):
         G.add_node(i,pos=(x_axis[i],y_axis[i]))

    for i in range(1,node):
        G.add_edge(p[i],i,weight=matrix[p[i]][i])

    pos=nx.get_node_attributes(G,'pos')
    nx.draw(G,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')



    plot.show()     


def dij(self,matrix,node,start_node,end_node,x_axis,y_axis):
    g1=Graph()

    
    for i in range(node):
        g1.add_vertex(i)


    for i in range(node):
        for  j in range(node):
            if matrix[i][j]!=0:
                #print(matrix[i][j])

                g1.add_edge(i,j,matrix[i][j])

    
    #pp=dijkstra(g1, 5)
    #g1.printer()
    pp=[]
    try:
        pp=g1.shortest_path(g1, start_node, end_node)
    except:
        self.output.setText("Edge doesn't exit between nodes")    
   # print(pp)

    


    G=nx.DiGraph()
    for i in range(node):
         G.add_node(i,pos=(x_axis[i],y_axis[i]))

    for i in range(len(pp)-1):
        G.add_edge(pp[i],pp[i+1],weight=matrix[pp[i]][pp[i+1]])

    pos=nx.get_node_attributes(G,'pos')
    nx.draw(G,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')



    plot.show()  








def original_graph(node,matrix,x_axis,y_axis):
    G=nx.DiGraph()
    for i in range(node):
        G.add_node(i,pos=(x_axis[i],y_axis[i]))


        
       

    for i in range(node):
        for j in range(node):
            if matrix[i][j]!=0:
                G.add_edge(i,j,weight=matrix[i][j])



    pos=nx.get_node_attributes(G,'pos')
#nx.draw(G,pos)
#plot.subplot(212); plot.axis('off')


    nx.draw_networkx_nodes(G,pos,
                           
                           node_color='b',
                           node_size=80,
                       alpha=0.5)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edges(G,pos,arrows=True,alpha=1, width=0.6)

    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,label_pos=0.6,font_size=8)
    nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
    plot.show()


#floyd1(matrix,node,4,5,x_axis,y_axis)
#plot.show()### showing graph

'''

    '''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
