class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countWays(n, arr, k):
        if k <= 0 or k >= n:
            return 0
        s = HashSet()
        for i in range(0, n):
            s.add(arr [i])
        if s.size() <= k:
            return 0
        return s.size() - k
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [100, 200, 400, 50]
        k = 3
        n = len(arr)
        print(GFG.countWays(n, arr, k))
