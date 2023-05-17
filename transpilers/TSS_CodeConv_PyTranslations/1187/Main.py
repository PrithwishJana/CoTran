import math

class Solution:
    @staticmethod
    def maxGCD(N, P):
        ans = 1
        prime_factors = {}
        i = 2
        while i * i <= P:
            while math.fmod(P, i) == 0:
                if prime_factors[i] is None:
                    prime_factors[i] = 1
                else:
                    prime_factors[i] = (prime_factors[i] + 1)
                P = math.trunc(P / float(i))
            i += 1
        if P != 1:
            if prime_factors[P] is None:
                prime_factors[P] = 1
            else:
                prime_factors[P] = (prime_factors[P] + 1)
        st = prime_factors.entrySet()
        for me in st:
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            ans *= me.getKey() ** (me.getValue() / N)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 3
        P = 24
        print(Solution.maxGCD(N, P))
