class GFG:
    adjacency = list  ()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def insert(x, y):
        GFG.adjacency[x].append(y)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def dfs(node, leaf, vis):
        leaf [node] = 0
        vis [node] = 1
        for i, unusedItem in enumerate(GFG.adjacency[node]):
            it = GFG.adjacency[node][i]
            if vis [it] == 0:
                GFG.dfs(it, leaf, vis)
                leaf [node] += leaf [it]
        if len(GFG.adjacency[node]) == 0:
            leaf [node] = 1
    @staticmethod
    def printLeaf(n, leaf):
        for i in range(1, n + 1):
            print("The node " + str(i) + " has " + str(leaf [i]) + " leaf nodes\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 6
        for i in range(0, N + 1):
            GFG.adjacency.append(list  ())
        GFG.insert(1, 2)
        GFG.insert(1, 3)
        GFG.insert(3, 4)
        GFG.insert(3, 5)
        GFG.insert(3, 6)
        leaf = [0 for _ in range(N + 1)]
        vis = [0 for _ in range(N + 1)]
        GFG.dfs(1, leaf, vis)
        GFG.printLeaf(N, leaf)
