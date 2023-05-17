class main:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        fr = FastReader()
        n = fr.nextInt()
        sum = 0
        total = 0
        i = 1
        if n == 2:
            print(1)
            return
        while n > 0:
            n -= 1
            if n > 0:
                if n >= 2:
                    total += 1
                n -= 2
            total += 1
        print(total)
    class FastReader:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
            self.st = java.util.StringTokenizer("")

        def next(self):
            while not self.st.hasMoreTokens():
                try:
                    self.st = java.util.StringTokenizer(self.br.readLine())
                except java.io.IOException as e:
                    pass
            return self.st.nextToken()
        def readArray(self, n):
            a = [0 for _ in range(n)]
            for i in range(0, n):
                a [i] = self.nextInt()
            return a
        def nextInt(self):
            return int(self.next())
        def nextLong(self):
            return int(self.next())
