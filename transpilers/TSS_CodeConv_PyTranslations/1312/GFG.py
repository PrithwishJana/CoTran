class GFG:
    @staticmethod
    def squareSum(n):
        sum = 0
        for i in range(1, n + 1):
            sum += (2 * i) * (2 * i)
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String args []) throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(GFG.squareSum(8))
