class GFG:
    @staticmethod
    def getMaxLength(arr, n):
        start = 0
        preCnt = 0
        while start < n and arr [start] == 1:
            preCnt += 1
            start += 1
        end = n - 1
        suffCnt = 0
        while end >= 0 and arr [end] == 1:
            suffCnt += 1
            end -= 1
        if start > end:
            return n
        midCnt = 0
        result = 0
        for i in range(start, end + 1):
            if arr [i] == 1:
                midCnt += 1
                result = max(result, midCnt)
            else:
                midCnt = 0
        return max(result, preCnt + suffCnt)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
        n = len(arr)
        print(GFG.getMaxLength(arr, n))
