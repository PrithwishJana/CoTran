import math

class Main:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws NumberFormatException, java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        pg = PrimeNumberGenerator()
        while True:
            n = int(br.readLine())
            if n == 0:
                break
            if pg.isPrime(n):
                print(0)
                continue
            begin = - 1
            end = - 1
            for i in range(n - 1, -1, -1):
                if pg.isPrime(i):
                    begin = i
                    break
            for i in range(n + 1, 2000000):
                if pg.isPrime(i):
                    end = i
                    break
            print(end - begin)
class PrimeNumberGenerator:
    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._N = 2000000
        self._isPrime = [False for _ in range(self._N + 1)]

        Arrays.fill(self._isPrime, True)
        self._isPrime [0] = False
        self._isPrime [1] = False
        limit = int(math.sqrt(self._N))
        for i in range(2, limit + 1):
            if self._isPrime [i] == False:
                continue
            j = i * 2
            while j <= self._N:
                self._isPrime [j] = False
                j += i
    def isPrime(self, index):
        return self._isPrime [index]
