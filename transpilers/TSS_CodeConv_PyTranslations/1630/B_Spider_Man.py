import math

class B_Spider_Man:
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
    scan = FastReader()
    @staticmethod
    def main(args):
        t = 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            B_Spider_Man.solve()
        t -= 1
    @staticmethod
    def solve():
        t = B_Spider_Man.scan.nextInt()
        arr = [0 for _ in range(t)]
        i = 0
        while i < len(arr):
            arr [i] = B_Spider_Man.scan.nextInt()
            i += 1
        prevWinner = 0
        i = 0
        while i < len(arr):
            if arr [i] == 1:
                if prevWinner == 0:
                    prevWinner = 2
            if prevWinner == 2 or prevWinner == 0:
                if math.fmod((arr [i] - 1), 2) == 0:
                    print(2)
                    prevWinner = 2
                else:
                    print(1)
                    prevWinner = 1
            else:
                if math.fmod((arr [i] - 1), 2) == 0:
                    print(1)
                    prevWinner = 1
                else:
                    print(2)
                    prevWinner = 2
            i += 1
