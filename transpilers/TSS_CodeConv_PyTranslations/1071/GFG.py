class GFG:
    @staticmethod
    def countIdenticalRows(mat):
        count = 0
        i = 0
        while i < len(mat):
            hs = java.util.HashSet()
            j = 0
            while j < len(mat [i]):
                hs.add(mat [i][j])
                j += 1
            if hs.size() == 1:
                count += 1
            i += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        mat = [[ 1, 1, 1 ], [ 1, 2, 3 ], [ 5, 5, 5 ]]
        print(GFG.countIdenticalRows(mat), end = '')
