class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def max(x, y):
        return x if (x > y) else y
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def lps(seq, i, j):
        if i == j:
            return 1
        if seq [i] == seq [j] and i + 1 == j:
            return 2
        if seq [i] == seq [j]:
            return GFG.lps(seq, i + 1, j - 1) + 2
        return GFG.max(GFG.lps(seq, i, j - 1), GFG.lps(seq, i + 1, j))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        seq = "GEEKSFORGEEKS"
        n = len(seq)
        print("The length of the LPS is {0:d}".format(GFG.lps(seq.toCharArray(), 0, n - 1)), end = '')
