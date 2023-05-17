import math

class Ishu:
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return Ishu.gcd(b, math.fmod(a, b))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        scan = java.util.Scanner(System.in)
        t = 0
        n = 0
        ans = 1
        t = scan.nextLong()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = scan.nextLong()
            ans = 1 + (math.trunc((4 * n) / float(Ishu.gcd(4 * n, n + 1))))
            print(ans)
        t -= 1
