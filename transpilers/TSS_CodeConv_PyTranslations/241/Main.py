import math

class Test:
    @staticmethod
    def FindLCM(a, b):
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        return (a * b) / (java.math.BigInteger(str(a) + "")).gcd(java.math.BigInteger(str(b) + "")).intValue()
    @staticmethod
    def rangeDivisor(m, n, a, b):
        lcm = Test.FindLCM(a, b)
        a_divisor = math.trunc(n / float(a)) - math.trunc((m - 1) / float(a))
        b_divisor = math.trunc(n / float(b)) - math.trunc((m - 1) / float(b))
        common_divisor = math.trunc(n / float(lcm)) - math.trunc((m - 1) / float(lcm))
        ans = a_divisor + b_divisor - common_divisor
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        m = 3
        n = 11
        a = 2
        b = 3
        print(Test.rangeDivisor(m, n, a, b))
        m = 11
        n = 1000000
        a = 6
        b = 35
        print(Test.rangeDivisor(m, n, a, b))
