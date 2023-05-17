class voting:
    @staticmethod
    def main(args):
        in_ = FScanner()
        out = PrintWriter(System.out)
        n = in_.nextInt()
        ans = 0
        max = 0
        a = [0 for _ in range(1000001)]
        for i in range(0, n):
            b = in_.nextInt()
            a [b] += 1
            if a [b] > max:
                max = a [b]
                ans = b
        out.print(ans)
        out.close()
    class FScanner:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = BufferedReader(InputStreamReader(System.in))
            self.sb = StringTokenizer("")

        def next(self):
            while not self.sb.hasMoreTokens():
                try:
                    self.sb = StringTokenizer(self.br.readLine())
                except IOException as e:
                    pass
            return self.sb.nextToken()
        def nextInt(self):
            return int(self.next())
        def nextLong(self):
            return int(self.next())
