class GFG:
    MAX = 100
    N = 0
    store = [0 for _ in range(MAX)]
    graph = [[0 for _ in range(MAX)] for _ in range(MAX)]
    d = [0 for _ in range(MAX)]
    @staticmethod
    def is_clique(b):
        for i in range(1, b):
            for j in range(i + 1, b):
                if GFG.graph [GFG.store [i]][GFG.store [j]] == 0:
                    return False
        return True
    @staticmethod
    def maxCliques(i, l):
        max_ = 0
        j = i + 1
        while j <= GFG.N:
            GFG.store [l] = j
            if GFG.is_clique(l + 1):
                max_ = max(max_, l)
                max_ = max(max_, GFG.maxCliques(j, l + 1))
            j += 1
        return max_
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        edges = [[ 1, 2 ], [ 2, 3 ], [ 3, 1 ], [ 4, 3 ], [ 4, 1 ], [ 4, 2 ]]
        size = len(edges)
        GFG.N = 4
        for i in range(0, size):
            GFG.graph [edges [i][0]][edges [i][1]] = 1
            GFG.graph [edges [i][1]][edges [i][0]] = 1
            GFG.d [edges [i][0]] += 1
            GFG.d [edges [i][1]] += 1
        print(GFG.maxCliques(0, 1))
