class Cv:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = FastScanner()
        sc = java.util.Scanner(System.in)
        o = java.io.PrintWriter(System.out)
        n = sc.nextInt()
        s = sc.nextInt()
        max = 0
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (n -- > 0)
        while n  > 0:
            n -= 1
            f = sc.nextInt()
            t = sc.nextInt()
            if max < f + t:
                max = f + t
        n -= 1
        o.println(max(max, s))
        o.close()
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
