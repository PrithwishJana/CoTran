import math

class A:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.in_ = None

    sc = None
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A.sc = FastReader()
        n = A.sc.nextInt()
        nax = 105
        a = A.sc.readArray(n)
        cnts = [0 for _ in range(nax)]
        for e in a:
            cnts [e + 1] += 1
        ans = 0
        pre = [0 for _ in range(nax)]
        for i in range(1, nax):
            pre [i] = pre [i - 1] + cnts [i]
            val = math.trunc((pre [i] + i - 1) / float(i))
            ans = max(ans, val)
        print(ans)
    @staticmethod
    def ruffleSort(a):
        al = []
        for i in a:
            al.append(i)
        al.sort()
        i = 0
        while i < len(a):
            a [i] = al[i]
            i += 1
        return a
    @staticmethod
    def print(a):
        for e in a:
            print(str(e) + " ", end = '')
        print()
    class FastReader:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.st = StringTokenizer("")
            self.br = BufferedReader(InputStreamReader(System.in))

        def next(self):
            while not self.st.hasMoreTokens():
                try:
                    self.st = StringTokenizer(self.br.readLine())
                except IOException as e:
                    e.printStackTrace()
            return self.st.nextToken()
        def nextInt(self):
            return int(self.next())
        def nextLong(self):
            return int(self.next())
        def readArray(self, n):
            a = [0 for _ in range(n)]
            for i in range(0, n):
                a [i] = A.sc.nextInt()
            return a
