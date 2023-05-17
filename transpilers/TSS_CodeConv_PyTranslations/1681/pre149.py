import math

#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math. *
class pre149:
    class FastReader:
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = None
            self.st = None

            self.br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        def next(self):
            while self.st is None or not self.st.hasMoreElements():
                try:
                    self.st = java.util.StringTokenizer(self.br.readLine())
                except java.io.IOException as e:
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
            except java.io.IOException as e:
                e.printStackTrace()
            return str
    @staticmethod
    def main(args):
        obj = FastReader()
        tc = obj.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (tc -- != 0)
        while tc  != 0:
            tc -= 1
            n = obj.nextInt()
            k = obj.nextInt()
            if n > k:
                print(math.trunc((k * (k + 1)) / float(2)))
            else:
                n -= 1
                n = math.trunc((n * (n + 1)) / float(2))
                n += 1
                print(n)
        tc -= 1
