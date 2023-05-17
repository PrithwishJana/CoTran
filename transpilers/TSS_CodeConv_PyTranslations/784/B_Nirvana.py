import math

class B_Nirvana:
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
        num = reader.nextInt()
        prod = 1
        ans = B_Nirvana.prodOfDigits(num)
        while num > 9:
            prod *= 9
            digit = math.fmod(num, 10)
            num = math.trunc(num / float(10))
            if digit == 9:
                ans = max(ans, B_Nirvana.prodOfDigits(int((num))) * prod)
            else:
                ans = max(ans, B_Nirvana.prodOfDigits(int((num - 1))) * prod)
                num = num - 1
        print(ans)
    @staticmethod
    def prodOfDigits(N):
        prod = 1
        while N != 0:
            digit = int((math.fmod(N, 10)))
            if digit == 0:
                return 0
            else:
                prod *= digit
                N = math.trunc(N / float(10))
        return prod
