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

    def __str__(self):
        s = ""
        l = [v for v in self.vertices]
        for x in l:
            s+="\n"
            s+="|" + str(x) + "| : "

            for y in self.vertices[x].connectedTo:
                s+=str(y)+ ":" + str(self.vertices[x].connectedTo[y])+ " " + "  "
        return s

g = Graph()

g.addEdge(0,1,0)
g.addEdge(0,2,3)
g.addEdge(0,3,2)
g.addEdge(1,3,1)
g.addEdge(2,3,1)

l = copy.deepcopy(g)

# choose the first node
vertlist = [x for x in l.vertices]
print(l)
accomodated_vertices = [vertlist[0]]
# get the lowest edge out of it
minEdge = 200
k = Graph()
while len(accomodated_vertices) < len(vertlist):
    for x in accomodated_vertices:
        for j in l.vertices[x].connectedTo:
            if j not in accomodated_vertices:
                if l.vertices[x].connectedTo[j] < minEdge:
                    minEdge = l.vertices[x].connectedTo[j]
                    minvertex1 = j
                    minvertex2 = x
    k.addEdge(minvertex2,minvertex1,minEdge)
    accomodated_vertices.append(minvertex1)
    print(accomodated_vertices)
    print(k)
    minEdge = 200



# print(accomodated_vertices)
# print(k)

# print (minEdge, "  ", minvertex)
