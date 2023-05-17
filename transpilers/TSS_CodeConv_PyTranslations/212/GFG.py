class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countSetBits(n):
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1
        return int(count)
    @staticmethod
    def countOfOddsPascal(n):
        c = GFG.countSetBits(n)
        return int(2) ** c
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 20
        print(GFG.countOfOddsPascal(n))
