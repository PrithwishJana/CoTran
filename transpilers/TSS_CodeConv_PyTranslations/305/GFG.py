class GFG:
    class pair:

        def _initialize_instance_fields(self):
            #instance fields found by Java to Python Converter:
            self.first = 0
            self.second = 0

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public pair(int first, int second)
        def __init__(self, first, second):
            self._initialize_instance_fields()

            self.first = first
            self.second = second
    N = 100005
    gr = [None for _ in range(N)]
    colour = [0 for _ in range(N)]
    edges = list  ()
    bip = False
    @staticmethod
    def add_edge(x, y):
        GFG.gr [x].append(y)
        GFG.gr [y].append(x)
        GFG.edges.append(pair(x, y))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def dfs(x, col):
        GFG.colour [x] = col
        for i in GFG.gr [x]:
            if GFG.colour [i] == - 1:
                GFG.dfs(i, col ^ 1)
            elif GFG.colour [i] == col:
                GFG.bip = False
    @staticmethod
    def Directed_Graph(n, m):
        i = 0
        while i < GFG.N:
            GFG.colour [i] = - 1
            i += 1
        GFG.bip = True
        GFG.dfs(1, 1)
        if not GFG.bip:
            print(- 1, end = '')
            return
        for i in range(0, m):
            if GFG.colour [GFG.edges[i].first] == 0:
                Collections.swap(GFG.edges, GFG.edges[i].first, GFG.edges[i].second)
            print(str(GFG.edges[i].first) + " " + str(GFG.edges[i].second))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        m = 3
        i = 0
        while i < GFG.N:
            GFG.gr [i] = list  ()
            i += 1
        GFG.add_edge(1, 2)
        GFG.add_edge(1, 3)
        GFG.add_edge(1, 4)
        GFG.Directed_Graph(n, m)
