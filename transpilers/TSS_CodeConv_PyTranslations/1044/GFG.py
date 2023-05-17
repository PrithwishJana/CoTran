class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printArray(arr, n):
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
    @staticmethod
    def getMin(arr, i, j):
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: int minVal = arr [i ++];
        minVal = arr [i ]
        i += 1
        while i <= j:
            minVal = min(minVal, arr [i])
            i += 1
        return minVal
    @staticmethod
    def getMax(arr, i, j):
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: int maxVal = arr [i ++];
        maxVal = arr [i ]
        i += 1
        while i <= j:
            maxVal = max(maxVal, arr [i])
            i += 1
        return maxVal
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def generateArr(arr, n):
        if n == 0:
            return
        if n == 1:
            print(arr [0])
            return
        tmpArr = [0 for _ in range(n)]
        tmpArr [0] = GFG.getMax(arr, 1, n - 1)
        i = 1
        while i < n - 1:
            tmpArr [i] = abs(GFG.getMax(arr, i + 1, n - 1) - GFG.getMin(arr, 0, i - 1))
            i += 1
        tmpArr [n - 1] = GFG.getMin(arr, 0, n - 2)
        GFG.printArray(tmpArr, n)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 5, 2, 4, 3]
        n = len(arr)
        GFG.generateArr(arr, n)
