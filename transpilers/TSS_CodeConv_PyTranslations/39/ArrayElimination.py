import math

class ArrayElimination:
    @staticmethod
    def main(args):
        scan = java.util.Scanner(System.in)
        t = scan.nextInt()
        for tt in range(0, t):
            n = scan.nextInt()
            bit = [0 for _ in range(32)]
            arr = [0 for _ in range(n)]
            for i in range(0, n):
                arr [i] = scan.nextInt()
            for i in range(0, n):
                for j in range(0, 32):
                    temp = (1 << (j - 1))
                    bitwiseAnd = arr [i] & temp
                    if bitwiseAnd > 0:
                        bit [j] += 1
            for i in range(1, n + 1):
                possible = True
                for j in range(0, 32):
                    if math.fmod(bit [j], i) != 0:
                        possible = False
                        break
                if possible:
                    print(str(i) + " ", end = '')
            print()
