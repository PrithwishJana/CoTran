class GFG:
    @staticmethod
    def printPairs(arr, n):
        v = list  ()
        for i in range(0, n):
            for j in range(i + 1, n):
                if abs(arr [i]) == abs(arr [j]):
                    v.append(abs(arr [i]))
        if len(v) == 0:
            return
        v.sort()
        for i, unusedItem in enumerate(v):
            print(- str(v[i]) + " " + str(v[i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 8, 9, - 4, 1, - 1, - 8, - 9]
        n = len(arr)
        GFG.printPairs(arr, n)
