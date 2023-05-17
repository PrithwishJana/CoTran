class GFG:
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        return self.countPaths(m - 1, n) + self.countPaths(m, n - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        g = GFG()
        n = 5
        m = 5
        print(g.countPaths(n, m))
