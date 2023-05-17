class GFG:
    arr = [1, 5, 6]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countWays(N):
        count = [0 for _ in range(N + 1)]
        count [0] = 1
        for i in range(1, N + 1):
            j = 0
            while j < len(GFG.arr):
                if i >= GFG.arr [j]:
                    count [i] += count [i - GFG.arr [j]]
                j += 1
        return count [N]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 7
        print("Total number of ways = " + str(GFG.countWays(N)))
