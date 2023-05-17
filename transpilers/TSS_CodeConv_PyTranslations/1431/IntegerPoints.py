import math

class IntegerPoints:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
        out = [0 for _ in range(t)]
        for i in range(0, t):
            n = sc.nextInt()
            p2 = 0
            for j in range(0, n):
                p2 += math.fmod((math.fmod(sc.nextInt(), 2) + 1), 2)
            m = sc.nextInt()
            q2 = 0
            for j in range(0, m):
                q2 += math.fmod((math.fmod(sc.nextInt(), 2) + 1), 2)
            out [i] = int(p2) * q2 + int((n - p2)) * (m - q2)
        for i in range(0, t):
            print(out [i])
