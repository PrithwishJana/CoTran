class Optimal_BST2:
    @staticmethod
    def optimalSearchTree(keys, freq, n):
        cost = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(0, n):
            cost [i][i] = freq [i]
        for L in range(2, n + 1):
            i = 0
            while i <= n - L + 1:
                j = i + L - 1
                cost [i][j] = Integer.MAX_VALUE
                for r in range(i, j + 1):
                    c = (cost [i][r - 1] if (r > i) else 0) + (cost [r + 1][j] if (r < j) else 0) + Optimal_BST2.sum(freq, i, j)
                    if c < cost [i][j]:
                        cost [i][j] = c
                i += 1
        return cost [0][n - 1]
    @staticmethod
    def sum(freq, i, j):
        s = 0
        for k in range(i, j + 1):
            if k >= len(freq):
                continue
            s += freq [k]
        return s
    @staticmethod
    def main(args):
        keys = [10, 12, 20]
        freq = [34, 8, 50]
        n = len(keys)
        print("Cost of Optimal BST is " + str(Optimal_BST2.optimalSearchTree(keys, freq, n)))
