import math

class main:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        chk = []
        for c1 in range('a', 'z' + 1):
            chk.append(c1 + "")
        for c1 in range('a', 'z' + 1):
            for c2 in range('a', 'z' + 1):
                chk.append(c1 + "" + c2)
        for c1 in range('a', 'z' + 1):
            for c2 in range('a', 'z' + 1):
                for c3 in range('a', 'z' + 1):
                    chk.append(c1 + "" + c2 + "" + c3)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = sc.nextInt()
            s = sc.next()
            for str in chk:
                if str in s:
                    continue
                print(str)
                break
        t -= 1
    @staticmethod
    def isPowerOfTen(input):
        if math.fmod(input, 10) != 0 or input == 0:
            return False
        if input == 10:
            return True
        return main.isPowerOfTen(math.trunc(input / float(10)))
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
