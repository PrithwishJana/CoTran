class GFG:
    @staticmethod
    def initializeDiffArray(A, D):
        n = len(A)
        D [0] = A [0]
        D [n] = 0
        for i in range(1, n):
            D [i] = A [i] - A [i - 1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def update(D, l, r, x):
        D [l] += x
        D [r + 1] -= x
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printArray(A, D):
        i = 0
        while i < len(A):
            if i == 0:
                A [i] = D [i]
            else:
                A [i] = D [i] + A [i - 1]
            print(str(A [i]) + " ", end = '')
            i += 1
        print()
        return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = [10, 5, 20, 40]
        n = len(A)
        D = [0 for _ in range(n + 1)]
        GFG.initializeDiffArray(A, D)
        GFG.update(D, 0, 1, 10)
        GFG.printArray(A, D)
        GFG.update(D, 1, 3, 20)
        GFG.update(D, 2, 2, 30)
        GFG.printArray(A, D)
