class GFG:
    @staticmethod
    def printLogestIncSubArr(arr, n):
        max = 1
        len = 1
        maxIndex = 0
        for i in range(1, n):
            if arr [i] > arr [i - 1]:
                len += 1
            else:
                if max < len:
                    max = len
                    maxIndex = i - max
                len = 1
        if max < len:
            max = len
            maxIndex = n - max
        i = maxIndex
        while i < max + maxIndex:
            print(str(arr [i]) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 6, 3, 5, 7, 8, 9, 1, 2]
        n = len(arr)
        GFG.printLogestIncSubArr(arr, n)
