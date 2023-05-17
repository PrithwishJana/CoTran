class GFG:
    @staticmethod
    def longestSubArray(arr, n):
        isZeroPresent = False
        for i in range(0, n):
            if arr [i] == 0:
                isZeroPresent = True
                break
        if isZeroPresent:
            return n
        return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 0, 1, 2, 0]
        n = len(arr)
        print(GFG.longestSubArray(arr, n))
