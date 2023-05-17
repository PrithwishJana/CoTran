class CF95A(PrintWriter):
    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.sc = Scanner(System.in)

        super().__init__(System.out, True)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main($):
        o = CF95A()
        o.main()
        o.flush()
    def compare(self, aa, i, bb, j, m):
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (m -- > 0)
        while m  > 0:
            m -= 1
            a = (aa [i]).upper()
            b = (bb [j]).upper()
            if a != b:
                return a - b
            i += 1
            j += 1
        m -= 1
        return 0
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(self):
        n = self.sc.nextInt()
        ss = [[] for _ in range(n)]
        for i in range(0, n):
            ss [i] = self.sc.next().toCharArray()
        cc = self.sc.next().toCharArray()
        m = len(cc)
        c = self.sc.next().charAt(0)
        c_ = c.upper()
        a = 'b' if c == 'a' else 'a'
        a_ = a.upper()
        lucky = [False for _ in range(m)]
        for j in range(0, m):
            for i in range(0, n):
                l = len(ss [i])
                if m - j >= l and self.compare(cc, j, ss [i], 0, l) == 0:
                    for h in range(0, l):
                        lucky [j + h] = True
        for j in range(0, m):
            if lucky [j]:
                if (cc [j]).casefold() == c:
                    cc [j] = a_ if (cc [j]).isupper() else a
                else:
                    cc [j] = c_ if (cc [j]).isupper() else c
        println(cc)
