import math

class main:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        k = sc.nextInt()
        arr = [0 for _ in range(n)]
        sum1 = 0
        sum2 = 0
        for i in range(0, n):
            arr [i] = sc.nextInt()
            sum1 = sum1 + arr [i]
        for i in range(1, n):
            csum = 0
            csum = arr [i] + arr [i - 1]
            if k > csum:
                arr [i] = arr [i] + k - csum
        for i in range(0, n):
            sum2 = sum2 + arr [i]
        print(sum2 - sum1)
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
        print()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if math.fmod(n, 2) == 0 or math.fmod(n, 3) == 0:
            return False
        i = 5
        while i * i <= n:
            if math.fmod(n, i) == 0 or math.fmod(n, (i + 2)) == 0:
                return False
            i = i + 6
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def gcd(a, b):
        if a == 0:
            return b
        return main.gcd(math.fmod(b, a), a)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def lcm(a, b):
        return (math.trunc(a / float(main.gcd(a, b)))) * b
