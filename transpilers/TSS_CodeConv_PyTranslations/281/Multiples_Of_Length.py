class Multiples_Of_Length:
    class FastReader:
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = None
            self.st = None

            self.br = BufferedReader(InputStreamReader(System.in))
        def next(self):
            while self.st is None or not self.st.hasMoreElements():
                try:
                    self.st = StringTokenizer(self.br.readLine())
                except IOException as e:
                    e.printStackTrace()
            return self.st.nextToken()
        def nextInt(self):
            return int(self.next())
        def nextLong(self):
            return int(self.next())
        def nextDouble(self):
            return float(self.next())
        def nextLine(self):
            str = ""
            try:
                str = self.br.readLine()
            except IOException as e:
                e.printStackTrace()
            return str
    @staticmethod
    def main(args):
        t = FastReader()
        o = PrintWriter(System.out)
        n = t.nextInt()
        a = [0 for _ in range(n)]
        for i in range(0, n):
            a [i] = t.nextLong()
        if n == 1:
            o.println("1 1")
            o.println(- a [0])
            o.println("1 1")
            o.println("0")
            o.println("1 1")
            o.println("0")
        else:
            o.println("1 1")
            o.println(- a [0])
            o.println("1 " + str(n))
            a [0] = 0
            for i in range(0, n):
                o.print(- str(n * a [i]) + " ")
            o.println("\n2 " + str(n))
            for i in range(1, n):
                o.print(str((n - 1) * a [i]) + " ")
        o.flush()
        o.close()
