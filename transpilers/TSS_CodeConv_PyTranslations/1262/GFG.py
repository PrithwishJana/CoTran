import math

class GFG:
    R = 4
    C = 4
    @staticmethod
    def first(arr, low, high):
        if high >= low:
            mid = low + math.trunc((high - low) / float(2))
            if (mid == 0 or arr [mid - 1] == 0) and arr [mid] == 1:
                return mid
            elif arr [mid] == 0:
                return GFG.first(arr, (mid + 1), high)
            else:
                return GFG.first(arr, low, (mid - 1))
        return - 1
    @staticmethod
    def rowWith0s(mat):
        max_row_index = 0
        max = Integer.MIN_VALUE
        min_row_index = 0
        min = Integer.MAX_VALUE
        i = 0
        index = 0
        i = 0
        while i < GFG.R:
            index = GFG.first(mat [i], 0, GFG.C - 1)
            cntZeroes = 0
            if index == - 1:
                cntZeroes = GFG.C
            else:
                cntZeroes = index
            if max < cntZeroes:
                max = cntZeroes
                max_row_index = i
            if min > cntZeroes:
                min = cntZeroes
                min_row_index = i
            i += 1
        print("Row with min 0s: " + str(min_row_index + 1))
        print("Row with max 0s: " + str(max_row_index + 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        mat = [[ 0, 0, 0, 1 ], [ 0, 1, 1, 1 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ]]
        GFG.rowWith0s(mat)
