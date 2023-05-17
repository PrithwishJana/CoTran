import math

class B215:
    @staticmethod
    def main(args):
        java.util.Locale.setDefault(java.util.Locale.US)
        in_ = java.util.Scanner(System.in)
        N = in_.nextInt()
        R1 = [0 for _ in range(N)]
        for n in range(0, N):
            R1 [n] = in_.nextInt()
        M = in_.nextInt()
        P1 = [0 for _ in range(M)]
        for m in range(0, M):
            P1 [m] = in_.nextInt()
        K = in_.nextInt()
        P2 = [0 for _ in range(K)]
        for k in range(0, K):
            P2 [k] = in_.nextInt()
        A = in_.nextInt()
        B = in_.nextInt()
        maxR1 = 0
        for r1 in R1:
            maxR1 = max(maxR1, r1)
        maxP1 = 0
        for p1 in P1:
            maxP1 = max(maxP1, p1)
        minP2 = Integer.MAX_VALUE
        for p2 in P2:
            minP2 = min(minP2, p2)
        r2 = math.sqrt(maxR1 * maxR1 * float(B) * maxP1 / (A * minP2 + B * maxP1))
        print(r2)
