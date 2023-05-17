class A111:
    fs = None
    @staticmethod
    def main(args):
        A111.fs = FastScanner()
        out = PrintWriter(System.out)
        n = A111.fs.nextLong()
        x = A111.fs.nextLong()
        y = A111.fs.nextLong()
        p = y - n + int(1)
        pow = p * p + n - int(1)
        if pow < x or p <= 0:
            out.println("-1")
        else:
            for i in range(1, n):
                out.println("1")
            out.println(p)
        out.println()
        out.close()
    @staticmethod
    def sort(a):
        l = []
        for i in a:
            l.append(i)
        l.sort()
        i = 0
        while i < len(a):
            a [i] = l[i]
            i += 1
    class FastScanner:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = BufferedReader(InputStreamReader(System.in))
            self.st = StringTokenizer("")

        def next(self):
            while not self.st.hasMoreTokens():
                try:
                    self.st = StringTokenizer(self.br.readLine())
                except IOException as e:
                    e.printStackTrace()
            return self.st.nextToken()
        def nextInt(self):
            return int(self.next())
        def readArray(self, n):
            a = [0 for _ in range(n)]
            for i in range(0, n):
                a [i] = self.nextInt()
            return a
        def nextLong(self):
            return int(self.next())
