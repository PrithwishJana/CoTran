import math

class CodeForces:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws FileNotFoundException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        fs = FastScanner()
        a = fs.nextInt()
        b = fs.nextInt()
        c = fs.nextInt()
        d = fs.nextInt()
        p = 0
        q = 0
        if a * d >= b * c:
            p = a * d - b * c
            q = a * d
        else:
            p = b * c - a * d
            q = b * c
        k = CodeForces.gcd(p, q)
        p = math.trunc(p / float(k))
        q = math.trunc(q / float(k))
        print(str(p) + "/" + str(q))
    @staticmethod
    def gcd(a, b):
        return a if b == 0 else CodeForces.gcd(b, math.fmod(a, b))
    @staticmethod
    def sort(a):
        l = []
        for i in a:
            l.append(i)
        l.sort()
        i = 0
        while i < len(a):
            a [i] = l[i]
            i += 1
    class FastScanner:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = BufferedReader(InputStreamReader(System.in))
            self.st = StringTokenizer("")

        def next(self):
            while not self.st.hasMoreTokens():
                try:
                    self.st = StringTokenizer(self.br.readLine())
                except IOException as e:
                    e.printStackTrace()
            return self.st.nextToken()
        def nextInt(self):
            return int(self.next())
        def readArray(self, n):
            a = [0 for _ in range(n)]
            for i in range(0, n):
                a [i] = self.nextInt()
            return a
        def nextLong(self):
            return int(self.next())
        def nextDouble(self):
            return float(self.next())
