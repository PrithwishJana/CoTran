import math

class Cv:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = FastScanner()
        sc = java.util.Scanner(System.in)
        out = java.io.PrintWriter(System.out)
        n = sc.nextInt()
        m = sc.nextInt()
        g = m
        f = 0
        sum = 0
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            arr [i] = sc.nextInt()
        for i in range(0, n):
            sum += arr [i]
            if m <= sum:
                f += math.trunc(sum / float(m))
                sum = math.fmod(sum, m)
            out.print(str(f) + " ")
            f -= f
        out.close()
    class FastScanner:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
            self.st = java.util.StringTokenizer("")

#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def next(self):
            while not self.st.hasMoreElements():
                try:
                    self.st = java.util.StringTokenizer(self.br.readLine())
                except java.io.IOException as e:
                    e.printStackTrace()
            return self.st.nextToken()
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def nextLine(self):
            str = ""
            try:
                str = self.br.readLine()
            except java.io.IOException as e:
                e.printStackTrace()
            return str
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def nextByte(self):
            return int(self.next())
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def nextShort(self):
            return int(self.next())
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def nextInt(self):
            return int(self.next())
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def nextLong(self):
            return int(self.next())
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def nextDouble(self):
            return float(self.next())
