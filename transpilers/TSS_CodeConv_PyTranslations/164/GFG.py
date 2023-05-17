class GFG:
    @staticmethod
    def CountSubSet(arr, n, X):
        N = int(2) ** n
        count = 0
        for i in range(0, N):
            for j in range(0, n):
                if (i & (1 << j)) != 0:
                    if arr [j] == X:
                        count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 5, 6, 7]
        X = 5
        n = len(arr)
        print(GFG.CountSubSet(arr, n, X))
