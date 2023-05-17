class p052:
    @staticmethod
    def main(args):
        print((p052()).run())
    def run(self):
        i = 1
        while True:
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            if i > Integer.MAX_VALUE / 6:
                raise ArithmeticException("Overflow")
            if p052._multiplesHaveSameDigits(i):
                return str(i)
            i += 1
    @staticmethod
    def _multiplesHaveSameDigits(x):
        for i in range(2, 7):
            if not java.util.Arrays.equals(p052._toSortedDigits(x), p052._toSortedDigits(i * x)):
                return False
        return True
    @staticmethod
    def _toSortedDigits(x):
        result = str(x).toCharArray()
        result.sort()
        return result
