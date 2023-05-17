import math

class Filling_Shapes:
    sc = java.util.Scanner(System.in)
    pw = java.io.PrintWriter(System.out)
    @staticmethod
    def main(args):
        n = Filling_Shapes.sc.nextInt()
        Filling_Shapes.pw.println(0 if (math.fmod(n, 2)) == 1 else int(2) ** math.trunc(n / float(2)))
        Filling_Shapes.pw.close()
    @staticmethod
    def find(n):
        arr = [0 for _ in range(60 + 1)]
        arr [1] = 0
        arr [2] = 2
        for i in range(3, n + 1):
            arr [i] = arr [i - 2] * 2
        return arr [n]
