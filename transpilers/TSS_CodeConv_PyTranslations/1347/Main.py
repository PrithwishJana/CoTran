class Graph:

    def _initialize_instance_fields(self):
        #instance fields found by Java to Python Converter:
        self._V = 0
        self._adj = None
        self._totalVertex = 0
        self._adjList = None

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: Graph(int v)
    def __init__(self, v):
        self._initialize_instance_fields()

        self._V = v
        self._adj = [None for _ in range(v)]
        for i in range(0, v):
            self._adj [i] = LinkedList()
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def addEdge(self, v, w):
        self._adj [v].add(w)
    def DFSUtil(self, v, visited):
        visited [v] = True
        print(str(v) + " ", end = '')
        i = self._adj [v].listIterator()
        while i.hasNext():
            n = i.next()
            if not visited [n]:
                self.DFSUtil(n, visited)
    def DFS(self, v):
        visited = [False for _ in range(self._V)]
        self.DFSUtil(v, visited)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        g = Graph(4)
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(1, 2)
        g.addEdge(2, 0)
        g.addEdge(2, 3)
        g.addEdge(3, 3)
        print("Following is Depth First Traversal (starting from vertex 2)")
        g.DFS(2)
