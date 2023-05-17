import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def calculate(x, k, m):
        result = x
        k -= 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (k -- > 0)
        while k  > 0:
            k -= 1
            result = int(result) ** x
            if result > m:
                result = math.fmod(result, m)
        k -= 1
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 5
        k = 2
        m = 3
        print(GFG.calculate(x, k, m))
