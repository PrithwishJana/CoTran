import math

class A:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.in_ = None

    sc = java.util.Scanner(System.in)
    cs = ['P', 'R', 'S']
    dp = [[None for _ in range(13)] for _ in range(3)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A.dp [0][0] = "P"
        A.dp [1][0] = "R"
        A.dp [2][0] = "S"
        i = 1
        while i < len(A.dp [0]):
            for j in range(0, 3):
                A.dp [j][i] = A.dp [j][i - 1] + A.dp [math.fmod((j + 1), 3)][i - 1]
                o = A.dp [math.fmod((j + 1), 3)][i - 1] + A.dp [j][i - 1]
                if o < A.dp [j][i]:
                    A.dp [j][i] = o
            i += 1
        T = A.sc.nextInt()
        for i in range(1, T + 1):
            print("Case #" + str(i) + ": ", end = '')
            print(A.solve())
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve():
        N = A.sc.nextInt()
        R = A.sc.nextInt()
        P = A.sc.nextInt()
        S = A.sc.nextInt()
        ret = None
        for i in range(0, 3):
            c = [0 for _ in range(3)]
            for ch in A.dp [i][N].toCharArray():
                if ch == 'P':
                    c [0] += 1
                if ch == 'R':
                    c [1] += 1
                if ch == 'S':
                    c [2] += 1
            if c [0] == P and c [1] == R and c [2] == S:
                ret = A.dp [i][N]
        return "IMPOSSIBLE" if ret is None else ret
