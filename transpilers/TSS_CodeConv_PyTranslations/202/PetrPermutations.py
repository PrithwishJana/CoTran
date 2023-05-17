import math

class PetrPermutations:
    @staticmethod
    def main(args):
        scanner = FastScanner()
        out = PrintWriter(System.out)
        N = scanner.nextInt()
        perm = [0 for _ in range(N)]
        for i in range(0, N):
            perm [i] = scanner.nextInt()
        swaps = 0
        vis = [False for _ in range(N)]
        for i in range(0, N):
            j = i
            cycle = 0
            while not vis [j]:
                vis [j] = True
                j = perm [j] - 1
                cycle += 1
            if cycle > 0:
                swaps += cycle - 1
        if math.fmod(swaps, 2) != math.fmod(N, 2):
            out.println("Um_nik")
        else:
            out.println("Petr")
        out.flush()
    class FastScanner:

        def _initialize_instance_fields(self):
            #instance fields found by Java to Python Converter:
            self.br = None
            self.st = None

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public FastScanner(Reader in)
        def __init__(self, in_):
            self._initialize_instance_fields()

            self.br = BufferedReader(in_)
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public FastScanner()
        def __init__(self):
            self(InputStreamReader(System.in))
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
        def readNextLine(self):
            str = ""
            try:
                str = self.br.readLine()
            except IOException as e:
                e.printStackTrace()
            return str
        def readIntArray(self, n):
            a = [0 for _ in range(n)]
            for idx in range(0, n):
                a [idx] = self.nextInt()
            return a
