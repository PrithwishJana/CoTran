class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countWays(n, arr, len):
        count = [0 for _ in range(n + 1)]
        count [0] = 1
        if n == 0:
            return 1
        for i in range(1, n + 1):
            no_ways = 0
            for j in range(0, len):
                if i - arr [j] >= 0:
                    no_ways += count [i - arr [j]]
                count [i] = no_ways
        return count [n]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 3, 5]
        len = len(arr)
        n = 5
        print(GFG.countWays(n, arr, len), end = '')
