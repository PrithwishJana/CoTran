class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isKthBitSet(x, k):
        rslt = 1 if ((x & (1 << (k - 1))) != 0) else 0
        return rslt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPalindrome(x):
        l = 1
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        r = (Integer.SIZE / 8) * 8
        while l < r:
            if GFG.isKthBitSet(x, l) != GFG.isKthBitSet(x, r):
                return 0
            l += 1
            r -= 1
        return 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 1 << 15 + 1 << 16
        print(GFG.isPalindrome(x))
        x = (1 << 31) + 1
        print(GFG.isPalindrome(x))
