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
