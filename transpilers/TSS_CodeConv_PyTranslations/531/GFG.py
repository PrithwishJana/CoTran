class GFG:
    pref = [0 for _ in range(100010)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPerfectCube(x):
        cr = round(Math.cbrt(x))
        if cr * cr * cr == float(x):
            return x
        return 0
    @staticmethod
    def compute():
        for i in range(1, 100001):
            GFG.pref [i] = GFG.pref [i - 1] + GFG.isPerfectCube(i)
    @staticmethod
    def printSum(L, R):
        sum = GFG.pref [R] - GFG.pref [L - 1]
        print(str(sum) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.compute()
        Q = 4
        arr = [[ 1, 10 ], [ 1, 100 ], [ 2, 25 ], [ 4, 50 ]]
        for i in range(0, Q):
            GFG.printSum(arr [i][0], arr [i][1])
