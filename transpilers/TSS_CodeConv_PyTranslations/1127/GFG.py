class GFG:
    @staticmethod
    def getLongestSeq(a, n):
        maxIdx = 0
        maxLen = 0
        currLen = 0
        currIdx = 0
        for k in range(0, n):
            if a [k] > 0:
                currLen += 1
                if currLen == 1:
                    currIdx = k
            else:
                if currLen > maxLen:
                    maxLen = currLen
                    maxIdx = currIdx
                currLen = 0
        if maxLen > 0:
            print("Index : " + str(maxIdx), end = '')
            print(" ,Length : " + str(maxLen), end = '')
        else:
            print("No positive sequence detected.")
        return
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, - 3, 2, 3, 4, - 6, 1, 2, 3, 4, 5, - 8, 5, 6]
        n = len(arr)
        GFG.getLongestSeq(arr, n)
