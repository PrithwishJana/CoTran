class GFG:
    maximum = Integer.MIN_VALUE
    x = 0
    ans = Integer.MAX_VALUE
    graph = list  ()
    weight = list  ()
    @staticmethod
    def __builtin_popcount(x):
        c = 0
        for i in range(0, 60):
            if ((x >> i) & 1) != 0:
                c += 1
        return c
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def dfs(node, parent):
        a = GFG.__builtin_popcount(GFG.weight[node] + GFG.x)
        if GFG.maximum < a:
            GFG.maximum = a
            GFG.ans = node
        elif GFG.maximum == a:
            GFG.ans = min(GFG.ans, node)
        for i, unusedItem in enumerate(GFG.graph[node]):
            if GFG.graph[node][i] == parent:
                continue
            GFG.dfs(GFG.graph[node][i], node)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.x = 15
        GFG.weight.append(0)
        GFG.weight.append(5)
        GFG.weight.append(10)
        pass
        GFG.weight.append(11)
        pass
        GFG.weight.append(8)
        GFG.weight.append(6)
        for i in range(0, 100):
            GFG.graph.append(list  ())
        GFG.graph[1].append(2)
        GFG.graph[2].append(3)
        GFG.graph[2].append(4)
        GFG.graph[1].append(5)
        GFG.dfs(1, 1)
        print(GFG.ans)
