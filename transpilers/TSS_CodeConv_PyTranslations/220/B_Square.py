class B_Square:
    class FastReader:
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = None
            self.st = None

            self.br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        def next(self):
            while self.st is None or not self.st.hasMoreElements():
                try:
                    self.st = StringTokenizer(self.br.readLine())
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
                if self.st.hasMoreTokens():
                    str = self.st.nextToken("\n")
                else:
                    str = self.br.readLine()
            except java.io.IOException as e:
                e.printStackTrace()
            return str
    @staticmethod
    def main(args):
        reader = FastReader()
        T = reader.nextInt()
        while T != 0:
            T -= 1
            a1 = reader.nextInt()
            b1 = reader.nextInt()
            a2 = reader.nextInt()
            b2 = reader.nextInt()
            r1 = [min(a1, b1), max(a1, b1)]
            r2 = [min(a2, b2), max(a2, b2)]
            if r1 [0] == r2 [0] and r1 [1] + r2 [1] == r1 [0]:
                print("Yes")
            elif r1 [1] == r2 [1] and r1 [0] + r2 [0] == r1 [1]:
                print("Yes")
            else:
                print("No")
