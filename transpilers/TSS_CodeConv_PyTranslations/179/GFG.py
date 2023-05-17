class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countNumbers(n):
        k = 0
        count = 0
        while n > 0:
            if (n & 1) == 0:
                count += int((2 ** k))
            k += 1
            n >>= 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 11
        print(GFG.countNumbers(n))
