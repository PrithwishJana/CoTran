class ValeraX:
    @staticmethod
    def main(args):
        cs = CustomScanner()
        n = cs.nextInt()
        xch = '\u0000'
        nxch = '\u0000'
        for i in range(0, n):
            line = cs.next()
            if i == 0:
                xch = line[0]
                nxch = line[1]
            if xch == nxch:
                print("NO")
                return
            for j in range(0, n):
                if j == i or j == n - i - 1:
                    if line[j] != xch:
                        print("NO")
                        return
                else:
                    if line[j] != nxch:
                        print("NO")
                        return
        print("YES")
    class CustomScanner:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
            self.st = java.util.StringTokenizer("")

        def next(self):
            while not self.st.hasMoreTokens():
                try:
                    self.st = java.util.StringTokenizer(self.br.readLine())
                except java.io.IOException as e:
                    e.printStackTrace()
            return self.st.nextToken()
        def nextInt(self):
            return int(self.next())
        def nextLong(self):
            return int(self.next())
        def readArray(self, n):
            a = [0 for _ in range(n)]
            for i in range(0, n):
                a [i] = self.nextInt()
            return a
