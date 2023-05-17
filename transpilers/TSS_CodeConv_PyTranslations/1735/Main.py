class KPaths:
    V = 4
    def countwalks(self, graph, u, v, k):
        if k == 0 and u == v:
            return 1
        if k == 1 and graph [u][v] == 1:
            return 1
        if k <= 0:
            return 0
        count = 0
        for i in range(0, KPaths.V):
            if graph [u][i] == 1:
                count += self.countwalks(graph, i, v, k - 1)
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
    def main(args):
        graph = [[ 0, 1, 1, 1 ], [ 0, 0, 0, 1 ], [ 0, 0, 0, 1 ], [ 0, 0, 0, 0 ]]
        u = 0
        v = 3
        k = 2
        p = KPaths()
        print(p.countwalks(graph, u, v, k))
