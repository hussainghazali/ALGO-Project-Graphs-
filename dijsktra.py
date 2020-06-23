from collections import defaultdict
import math 



class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_vertex(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    if(to_node==6 ):
      print(from_node)
      #print(to_node)

    self.edges[from_node].append(to_node)
    #self.edges[to_node].append(from_node)

    self.distances[(from_node, to_node)] = distance

  def shortest_path(self,graph, start, end):
      #print(start,'ssd')
      delta, previous = self.dijkstra(graph,start)
      
      path = []
      vertex = end

      while vertex is not None:

        path.append(vertex)
        if(vertex==start):
          break
        vertex = previous[vertex]


      path.reverse()
      return path
  def dijkstra(self,graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes: 
      min_node = None
      for node in nodes:
        if node in visited:
          if min_node is None:
            min_node = node
          elif visited[node] < visited[min_node]:
            min_node = node

      if min_node is None:
        break

      nodes.remove(min_node)
      current_weight = visited[min_node]

      for edge in graph.edges[min_node]:
        
        weight = current_weight + graph.distances[(min_node, edge)]
        '''
        except:
          weight = current_weight + graph.distances[(edge, min_node)]
        '''
        if edge not in visited or weight < visited[edge]:
          visited[edge] = weight
          path[edge] = min_node

    return (visited, path)

  def printer(self):
      for edge in self.edges[6]:
        print(edge)