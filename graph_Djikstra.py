import copy
from collections import deque
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
g.addEdge(0,1,3)
g.addEdge(0,2,5)
g.addEdge(0,3,1)
g.addEdge(1,4,2)
g.addEdge(1,5,10)
g.addEdge(2,3,2)
g.addEdge(2,4,1)
g.addEdge(4,5,2)



print(g)

l = copy.deepcopy(g)

# time to djikstra this
vertlist = [x for x in l.vertices]
resTable = { x : 20000 for x in vertlist}
resTable[0] = 0
vertStack = deque([])
vertStack.append(0)
currNodeDistance = 0f

while len(vertStack) != 0:
    currNode = vertStack.popleft()
    currNodeDistance = resTable[currNode]
    tempStack = []
    popStack = []
    for key,val in l.vertices[currNode].connectedTo.items():
        if(resTable[key]>val+currNodeDistance):
            resTable[key] = val+currNodeDistance
            tempStack.append(key)
        popStack.append(key)

    for key in popStack:
        l.vertices[currNode].connectedTo.pop(key)
    vertStack.extend(sorted(tempStack))

print(resTable)
