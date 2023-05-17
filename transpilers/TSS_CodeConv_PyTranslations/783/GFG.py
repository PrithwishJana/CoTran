class GFG:
    N = 1000001
    c = 0
    N = 0
    m = 0
    a = 0
    b = 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def dfs(a, b, v, vis):
        vis [a] = 1
        GFG.c += 1
        for i in v [a]:
            if vis [i] == 0 and i != b:
                GFG.dfs(i, b, v, vis)
    @staticmethod
    def Calculate(v):
        vis = [0 for _ in range(GFG.N + 1)]
        Arrays.fill(vis, 0)
        GFG.c = 0
        GFG.dfs(GFG.a, GFG.b, v, vis)
        ans1 = GFG.N - GFG.c - 1
        Arrays.fill(vis, 0)
        GFG.c = 0
        GFG.dfs(GFG.b, GFG.a, v, vis)
        ans2 = GFG.N - GFG.c - 1
        print(str(ans1 * ans2) + "\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.N = 7
        GFG.m = 7
        GFG.a = 3
        GFG.b = 5
        edges = [[ 1, 2 ], [ 2, 3 ], [ 3, 4 ], [ 4, 5 ], [ 5, 6 ], [ 6, 7 ], [ 7, 5 ]]
        v = [None for _ in range(GFG.N + 1)]
        i = 0
        while i <= GFG.N:
            v [i] = list  ()
            i += 1
        i = 0
        while i < GFG.m:
            v [edges [i][0]].append(edges [i][1])
            v [edges [i][1]].append(edges [i][0])
            i += 1
        GFG.Calculate(v)
