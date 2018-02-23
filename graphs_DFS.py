import copy
class Vertex:
    def __init__(self,key):
        self.connectedTo = {}
        self.key = key

class Graph:
    def __init__(self):
        self.vertices = {}

    def addEdge(self,v1,v2, cost = 0, undirected = True):
        self.addVertex(v1)
        self.addVertex(v2)
        self.vertices[v1].connectedTo[v2] = cost
        if undirected:
            self.vertices[v2].connectedTo[v1] = cost

    def removeEdge(self,v1,v2,undirected = True):
        self.vertices[v1].connectedTo.pop(v2,None)
        if undirected:
            self.vertices[v2].connectedTo.pop(v1,None)

    def addVertex(self,v):
        if v not in self.vertices:
            nv = Vertex(v)
            self.vertices[v] = nv

def DFS_graph(g,currNode,visited):
    visited[currNode] = True
    print(currNode)
    for x in g.vertices[currNode].connectedTo:
        if visited[x] == False:
            visited[x] = True
            DFS_graph(g,x,visited)

g = Graph()
g.addEdge(0,1,3)
g.addEdge(0,2,5)
g.addEdge(0,3,1)
g.addEdge(1,4,2)
g.addEdge(1,5,10)
g.addEdge(2,3,2)
g.addEdge(2,4,1)
g.addEdge(4,5,2)

visitedList = [ False for x in range(6)]
print(visitedList)
DFS_graph(g,0,visitedList)
