class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printDistinct(arr, n):
        Arrays.sort(arr)
        i = 0
        while i < n:
            while i < n - 1 and arr [i] == arr [i + 1]:
                i += 1
            print(str(arr [i]) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
        n = len(arr)
        GFG.printDistinct(arr, n)
