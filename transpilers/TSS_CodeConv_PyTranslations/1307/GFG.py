class GFG:
    @staticmethod
    def squaresum(n):
        sum = 0
        for i in range(1, n + 1):
            sum += (i * i)
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String args []) throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        print(GFG.squaresum(n))
