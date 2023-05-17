class DmwS:
    below = None
    vis = None
    result = 0
    K = 0
    adj = None
    unis = None
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        N = sc.nextInt()
        DmwS.K = sc.nextInt()
        DmwS.adj = [None for _ in range(N)]
        DmwS.unis = [0 for _ in range(N)]
        for i in range(0, N):
            DmwS.adj [i] = LinkedList()
        i = 0
        while i < 2 * DmwS.K:
            town = sc.nextInt() - 1
            DmwS.unis [town] += 1
            i += 1
        i = 0
        while i < N - 1:
            x = sc.nextInt() - 1
            y = sc.nextInt() - 1
            DmwS.adj [x].add(y)
            DmwS.adj [y].add(x)
            i += 1
        DmwS.below = [0 for _ in range(N)]
        DmwS.vis = [False for _ in range(N)]
        DmwS.dfs(0)
        print(DmwS.result)
    @staticmethod
    def dfs(node):
        DmwS.vis [node] = True
        DmwS.below [node] = DmwS.unis [node]
        for adj in adj [node]:
            if DmwS.vis [adj]:
                continue
            DmwS.dfs(adj)
            DmwS.below [node] += DmwS.below [adj]
            DmwS.result += min(DmwS.below [adj], 2 * DmwS.K - DmwS.below [adj])
