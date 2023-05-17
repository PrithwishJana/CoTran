import math

class Task:
    scanner = java.util.Scanner(System.in)
    @staticmethod
    def main(args):
        n = Task.scanner.nextInt()
        p = [0 for _ in range(n)]
        for i in range(0, n):
            p [i] = Task.scanner.nextInt()
        onlyFistSolve = 0
        onlySecondSolve = 0
        for i in range(0, n):
            r = Task.scanner.nextInt()
            if p [i] == 1 and r == 0:
                onlyFistSolve += 1
            elif p [i] == 0 and r == 1:
                onlySecondSolve += 1
        if onlyFistSolve == 0:
            print(- 1)
        else:
            print(math.trunc((onlySecondSolve + onlyFistSolve) / float(onlyFistSolve)))
