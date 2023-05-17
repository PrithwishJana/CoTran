class GFG:
    @staticmethod
    def printLastOccurrence(a, n):
        map = {}
        for i in range(0, n):
            map[a [i]] = i
        for i in range(0, n):
            if map[a [i]] == i:
                print(str(a [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 5, 5, 1, 6, 1]
        n = len(a)
        GFG.printLastOccurrence(a, n)
