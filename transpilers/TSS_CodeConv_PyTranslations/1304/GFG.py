import math

class GFG:
    @staticmethod
    def aliquotSum(n):
        sum = 0
        for i in range(1, n):
            if math.fmod(n, i) == 0:
                sum += i
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String args []) throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 12
        print(GFG.aliquotSum(n))
