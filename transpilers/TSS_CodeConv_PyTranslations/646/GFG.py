class GFG:
    @staticmethod
    def zeroUpto(digits):
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        first = int(((10 ** digits - 1) / 9))
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        second = int(((9 ** digits - 1) / 8))
        return 9 * (first - second)
    @staticmethod
    def toInt(c):
        return ord((c)) - 48
    @staticmethod
    def countZero(num):
        k = len(num)
        total = GFG.zeroUpto(k - 1)
        non_zero = 0
        i = 0
        while i < len(num):
            if num[i] == '0':
                non_zero -= 1
                break
            non_zero += (GFG.toInt(num[i]) - 1) * (9 ** (k - 1 - i))
            i += 1
        no = 0
        remaining = 0
        calculatedUpto = 0
        i = 0
        while i < len(num):
            no = no * 10 + (GFG.toInt(num[i]))
            if i != 0:
                calculatedUpto = calculatedUpto * 10 + 9
            i += 1
        remaining = no - calculatedUpto
        ans = GFG.zeroUpto(k - 1) + (remaining - non_zero - 1)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        num = "107"
        print("Count of numbers from 1" + " to " + num + " is " + str(GFG.countZero(num)))
        num = "1264"
        print("Count of numbers from 1" + " to " + num + " is " + str(GFG.countZero(num)))
