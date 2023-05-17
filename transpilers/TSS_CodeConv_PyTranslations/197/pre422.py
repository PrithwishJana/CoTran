import math

class pre422:
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
        s = [None for _ in range(1000)]
        for n in range(1, 1001):
            flag = True
            for i in range(0, 1001):
                for j in range(0, 1001):
                    if math.fmod((n - i * 3 - j * 5), 7) == 0 and math.trunc((n - i * 3 - j * 5) / float(7)) >= 0:
                        s [n - 1] = (i + " " + j + " " + math.trunc((n - i * 3 - j * 5) / float(7)))
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                s [n - 1] = "-1"
        tc = obj.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (tc -- != 0)
        while tc  != 0:
            tc -= 1
            n = obj.nextInt()
            print(s [n - 1])
        tc -= 1
