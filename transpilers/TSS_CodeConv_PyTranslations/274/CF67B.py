class CF67B(PrintWriter):
    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.sc = Scanner(System.in)

        super().__init__(System.out, True)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main($):
        o = CF67B()
        o.main()
        o.flush()
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(self):
        n = self.sc.nextInt()
        k = self.sc.nextInt()
        bb = [0 for _ in range(n)]
        for i in range(0, n):
            bb [i] = self.sc.nextInt()
        aa = [0 for _ in range(n)]
        m = 0
        for a in range(n - 1, -1, -1):
            j = 0
            while bb [a] > 0:
                if aa [j] >= a + k:
                    bb [a] -= 1
                j += 1
            int j_ = m = int j_ = m + 1
            while j_ > j:
                aa [j_] = aa [j_ - 1]
                j_ -= 1
            aa [j] = a
        for i in range(0, n):
            print(str(aa [i]) + str(1) + " ")
        println()
