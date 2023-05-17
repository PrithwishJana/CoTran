class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def updateArray(arr, n):
        for i in range(n - 1, 0, -1):
            arr [i] = arr [i - 1]
        arr [0] = - 1
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 1, 3, 2, 4]
        N = len(arr)
        GFG.updateArray(arr, N)
