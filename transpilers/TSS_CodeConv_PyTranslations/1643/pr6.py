import math

class pr6:
    @staticmethod
    def main(args):
        scan = Scanner(System.in)
        n = scan.nextInt()
        k1 = 0
        k2 = 0
        w1 = 0
        w2 = 0
        a = [0 for _ in range(n)]
        for i in range(0, n):
            a [i] = scan.nextInt()
            if math.fmod(a [i], 2) == 0:
                w1 += 1
                k1 = i + 1
            else:
                w2 += 1
                k2 = i + 1
        print(k1 if (w1 == 1) else k2)
