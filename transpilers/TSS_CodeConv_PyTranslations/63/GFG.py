class GFG:
    @staticmethod
    def printConsecutive(last, first):
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: System.out.print(first ++);
        print(first, end = '')
        first += 1
        for x in range(first, last + 1):
            print(" + " + str(x), end = '')
    @staticmethod
    def findConsecutive(N):
        for last in range(1, N):
            for first in range(0, last):
                if 2 * N == (last - first) * (last + first + 1):
                    print(str(N) + " = ", end = '')
                    GFG.printConsecutive(last, first + 1)
                    return
        print("-1", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 12
        GFG.findConsecutive(n)
