class GFG:
    M = 4
    N = 5
    @staticmethod
    def printCommonElements(mat):
        mp = {}
        j = 0
        while j < GFG.N:
            mp[mat [0][j]] = 1
            j += 1
        i = 1
        while i < GFG.M:
            j = 0
            while j < GFG.N:
                if mp[mat [i][j]] is not None and mp[mat [i][j]] == i:
                    mp[mat [i][j]] = i + 1
                    if i == GFG.M - 1:
                        print(str(mat [i][j]) + " ", end = '')
                j += 1
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        mat = [[ 1, 2, 1, 4, 8 ], [ 3, 7, 8, 5, 1 ], [ 8, 7, 7, 3, 1 ], [ 8, 1, 2, 7, 9 ]]
        GFG.printCommonElements(mat)
