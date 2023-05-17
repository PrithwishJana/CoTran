class GFG:
    N = 5005
    N = 0
    k = 0
    gr = [None for _ in range(N)]
    d = [[0 for _ in range(505)] for _ in range(N)]
    ans = 0
    @staticmethod
    def Add_edge(x, y):
        GFG.gr [x].append(y)
        GFG.gr [y].append(x)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def dfs(v, par):
        GFG.d [v][0] = 1
        for i in GFG.gr [v]:
            if i != par:
                GFG.dfs(i, v)
                j = 1
                while j <= GFG.k:
                    GFG.ans += GFG.d [i][j - 1] * GFG.d [v][GFG.k - j]
                    j += 1
                j = 1
                while j <= GFG.k:
                    GFG.d [v][j] += GFG.d [i][j - 1]
                    j += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.N = 5
        GFG.k = 2
        i = 0
        while i < GFG.N:
            GFG.gr [i] = list  ()
            i += 1
        GFG.Add_edge(1, 2)
        GFG.Add_edge(2, 3)
        GFG.Add_edge(3, 4)
        GFG.Add_edge(2, 5)
        GFG.dfs(1, 0)
        print(GFG.ans, end = '')
