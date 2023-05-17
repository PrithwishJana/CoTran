import math

class GFG:
    @staticmethod
    def maximumXOR(n, l, r):
        x = 0
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        for i in range(int((math.log(r) / math.log(2))), -1, -1):
            if (n & (1 << i)) > 0:
                if (x > r) or (x + (1 << i) - 1 < l):
                    x ^= (1 << i)
            else:
                if (x ^ (1 << i)) <= r:
                    x ^= (1 << i)
        return n ^ x
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 7
        l = 2
        r = 23
        print("The output is " + str(GFG.maximumXOR(n, l, r)))
