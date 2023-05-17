import math

class p033:
    @staticmethod
    def main(args):
        print((p033()).run())
    def run(self):
        numer = 1
        denom = 1
        for d in range(10, 100):
            for n in range(10, d):
                n0 = math.fmod(n, 10)
                n1 = math.trunc(n / float(10))
                d0 = math.fmod(d, 10)
                d1 = math.trunc(d / float(10))
                if n1 == d0 and n0 * d == n * d1 or n0 == d1 and n1 * d == n * d0:
                    numer *= n
                    denom *= d
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        return str(denom / Library.gcd(numer, denom))
