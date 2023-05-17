class GFG:
    @staticmethod
    def maxAbsDiff(arr, n):
        minEle = arr [0]
        maxEle = arr [0]
        for i in range(1, n):
            minEle = min(minEle, arr [i])
            maxEle = max(maxEle, arr [i])
        return (maxEle - minEle)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 1, 5, 3]
        n = len(arr)
        print(GFG.maxAbsDiff(arr, n), end = '')
