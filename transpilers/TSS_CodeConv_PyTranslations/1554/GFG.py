class GFG:
    @staticmethod
    def countBits(n):
        count = 0
        while n != 0:
            count += 1
            n >>= 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        i = 65
        print(GFG.countBits(i), end = '')
