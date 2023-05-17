class GFG:
    @staticmethod
    def printElements(arr, n):
        i = 1
        while i < n - 1:
            if arr [i] > arr [i - 1] and arr [i] > arr [i + 1]:
                print(str(arr [i]) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 1, 5, 4, 9, 8, 7, 5]
        n = len(arr)
        GFG.printElements(arr, n)
