import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def rearrange(arr):
        if arr is None or math.fmod(len(arr), 2) == 1:
            return
        currIdx = math.trunc((len(arr) - 1) / float(2))
        while currIdx > 0:
            count = currIdx
            swapIdx = currIdx
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (count -- > 0)
            while count  > 0:
                count -= 1
                temp = arr [swapIdx + 1]
                arr [swapIdx + 1] = arr [swapIdx]
                arr [swapIdx] = temp
                swapIdx += 1
            count -= 1
            currIdx -= 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 3, 5, 2, 4, 6]
        GFG.rearrange(arr)
        i = 0
        while i < len(arr):
            print(" " + str(arr [i]), end = '')
            i += 1
