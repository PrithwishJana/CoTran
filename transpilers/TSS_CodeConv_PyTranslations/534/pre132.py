#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math. *
class pre132:
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
            arr = obj.next().toCharArray()
            r = n - 1
            l = - 1
            while r >= 0 and arr [r] == '1':
                r -= 1
            while l + 1 < n and arr [0] == '0' and arr [l + 1] == '0':
                l += 1
            flag = [False for _ in range(n)]
            for i in range(0, l + 1):
                flag [i] = True
            i = n - 1
            while i >= r and i >= 0:
                flag [i] = True
                i -= 1
            for i in range(0, n):
                if flag [i]:
                    print(arr [i], end = '')
            print()
        tc -= 1
