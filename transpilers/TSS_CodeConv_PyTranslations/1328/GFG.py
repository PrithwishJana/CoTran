class GFG:
    @staticmethod
    def printPermutation(n, k):
        i = 0
        mx = n
        for i in range(1, k + 1):
            print(str(mx) + " ", end = '')
            mx -= 1
        for i in range(1, mx + 1):
            print(str(i) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 5
        K = 3
        if K >= N - 1:
            print("Not Possible", end = '')
        else:
            GFG.printPermutation(N, K)
