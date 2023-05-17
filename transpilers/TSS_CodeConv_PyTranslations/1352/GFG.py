class GFG:
    m = 6
    N = 4
    @staticmethod
    def linearCheck(ar, arr):
        i = 0
        while i < GFG.m:
            matched = True
            j = 0
            while j < GFG.N:
                if ar [i][j] != arr [j]:
                    matched = False
                    break
                j += 1
            if matched:
                return i + 1
            i += 1
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        mat = [[ 0, 0, 1, 0 ], [ 10, 9, 22, 23 ], [ 40, 40, 40, 40 ], [ 43, 44, 55, 68 ], [ 81, 73, 100, 132 ], [ 100, 75, 125, 133 ]]
        row = [10, 9, 22, 23]
        print(GFG.linearCheck(mat, row))
