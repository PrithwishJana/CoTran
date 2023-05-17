class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findElements(arr, n):
        Arrays.sort(arr)
        i = 0
        while i < n - 2:
            print(str(arr [i]) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, - 6, 3, 5, 1]
        n = len(arr)
        GFG.findElements(arr, n)
