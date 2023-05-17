class GFG:
    @staticmethod
    def sortSquares(arr):
        n = len(arr)
        for i in range(0, n):
            arr [i] = arr [i] * arr [i]
        Arrays.sort(arr)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [- 6, - 3, - 1, 2, 4, 5]
        n = len(arr)
        print("Before sort")
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
        GFG.sortSquares(arr)
        print("")
        print("After sort")
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
