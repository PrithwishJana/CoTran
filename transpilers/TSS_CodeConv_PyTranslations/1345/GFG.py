class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPerfectCube(x):
        cr = int(Math.cbrt(x))
        return (cr * cr * cr == x)
    @staticmethod
    def canBePerfectCube(N, K):
        if GFG.isPerfectCube(N + K) or GFG.isPerfectCube(N - K) == True:
            print("Yes")
        else:
            print("No")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 7
        K = 1
        GFG.canBePerfectCube(N, K)
        N = 5
        K = 4
        GFG.canBePerfectCube(N, K)
        N = 7
        K = 2
        GFG.canBePerfectCube(N, K)
