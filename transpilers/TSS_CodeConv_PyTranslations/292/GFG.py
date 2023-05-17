class GFG:
    @staticmethod
    def maxOR(arr, n):
        maxVal = 0
        i = 0
        while i < n - 1:
            for j in range(i + 1, n):
                maxVal = max(maxVal, arr [i] | arr [j])
            i += 1
        return maxVal
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 8, 12, 16]
        n = len(arr)
        print(GFG.maxOR(arr, n))
