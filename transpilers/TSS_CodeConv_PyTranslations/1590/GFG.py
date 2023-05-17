class GFG:
    R = 4
    C = 4
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPaths(maze):
        if maze [0][0] == - 1:
            return 0
        i = 0
        while i < GFG.R:
            if maze [i][0] == 0:
                maze [i][0] = 1
            else:
                break
            i += 1
        i = 1
        while i < GFG.C:
            if maze [0][i] == 0:
                maze [0][i] = 1
            else:
                break
            i += 1
        i = 1
        while i < GFG.R:
            j = 1
            while j < GFG.C:
                if maze [i][j] == - 1:
                    j += 1
                    continue
                if maze [i - 1][j] > 0:
                    maze [i][j] = (maze [i][j] + maze [i - 1][j])
                if maze [i][j - 1] > 0:
                    maze [i][j] = (maze [i][j] + maze [i][j - 1])
                j += 1
            i += 1
        return maze [GFG.R - 1][GFG.C - 1] if (maze [GFG.R - 1][GFG.C - 1] > 0) else 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        maze = [[ 0, 0, 0, 0 ], [ 0, - 1, 0, 0 ], [ - 1, 0, 0, 0 ], [ 0, 0, 0, 0 ]]
        print(GFG.countPaths(maze))
