class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def updateArray(arr, n):
        i = 0
        while i <= n - 2:
            arr [i] = arr [i + 1]
            i += 1
        arr [n - 1] = - 1
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 1, 3, 2, 4]
        N = len(arr)
        GFG.updateArray(arr, N)
