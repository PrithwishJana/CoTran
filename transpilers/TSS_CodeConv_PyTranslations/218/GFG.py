class GFG:
    @staticmethod
    def _printPaths(input, R, C):
        for i in range(0, C):
            GFG._dfs(input, "", 0, i, R, C)
            print()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def _dfs(input, res, i, j, R, C):
        if i == R:
            print(res + " ", end = '')
            return
        res = res + input [i][j]
        for k in range(0, C):
            GFG._dfs(input, res, i + 1, k, R, C)
            if i + 1 == R:
                break
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        input = [[ 'a', 'b' ], [ 'd', 'e' ]]
        R = len(input)
        C = len(input [0])
        GFG._printPaths(input, R, C)
