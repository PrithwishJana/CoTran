class CF862B:
    arr = None
    totalFalse = 0
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        n = sc.nextInt()
        CF862B.arr = [None for _ in range(n)]
        CF862B.totalFalse = 0
        for i in range(0, n):
            CF862B.arr [i] = Node(i)
        i = 0
        while i < n - 1:
            a = sc.nextInt() - 1
            b = sc.nextInt() - 1
            CF862B.arr [a].neighbors.append(b)
            CF862B.arr [b].neighbors.append(a)
            i += 1
        CF862B.dfs(0, True)
        total = 0
        for i in range(0, n):
            if CF862B.arr [i].parity:
                total += (CF862B.totalFalse - len(CF862B.arr [i].neighbors))
        print(total)
    @staticmethod
    def dfs(currNode, parity):
        CF862B.arr [currNode].parity = parity
        if not parity:
            CF862B.totalFalse += 1
        for nextNode in CF862B.arr [currNode].neighbors:
            if CF862B.arr [nextNode].parity is not None:
                continue
            CF862B.dfs(nextNode, (not parity))
    class Node:
        def __init__(self, index):
            #instance fields found by Java to Python Converter:
            self.index = 0
            self.neighbors = None
            self.parity = False

            self.index = index
            self.neighbors = []
            self.parity = None
