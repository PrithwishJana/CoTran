import math

class Forming_Teams:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.count = 0
        self.seen = None
        self.path = 0
        self.cycle = 1
        self.graph = None

    def dfs(self, child, par):
        if self.seen [child] == True:
            return self.cycle
        self.seen [child] = True
        for i in self.graph.get(child):
            if i != par:
                self.count += 1
                if self.dfs(i, child) == self.cycle:
                    return self.cycle
        return self.path
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        m = sc.nextInt()
        n = sc.nextInt()
        ft = Forming_Teams()
        ft.graph = java.util.LinkedList()
        for i in range(0, m + 1):
            ft.graph.add(java.util.LinkedList())
        ft.seen = [False for _ in range(m + 1)]
        for i in range(0, n):
            x = sc.nextInt()
            y = sc.nextInt()
            ft.graph.get(x).add(y)
            ft.graph.get(y).add(x)
        toremove = 0
        for i in range(1, m + 1):
            if not ft.seen [i]:
                ft.count = 0
                if ft.dfs(i, 0) == ft.cycle:
                    if math.fmod(ft.count, 2) == 1:
                        toremove += 1
        if math.fmod((m - toremove), 2) == 1:
            toremove += 1
        print(toremove)
