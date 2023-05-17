class A354:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        N = in_.nextInt()
        L = in_.nextInt()
        R = in_.nextInt()
        QL = in_.nextInt()
        QR = in_.nextInt()
        W = [0 for _ in range(N)]
        sum = [0 for _ in range(N + 1)]
        for n in range(0, N):
            W [n] = in_.nextInt()
            sum [n + 1] = sum [n] + W [n]
        min = Long.MAX_VALUE
        for firstR in range(0, N + 1):
            lCount = firstR
            rCount = N - lCount
            cand = sum [lCount] * L + (sum [N] - sum [lCount]) * R
            llCount = max(0, lCount - rCount - 1)
            rrCount = max(0, rCount - lCount - 1)
            cand += llCount * QL
            cand += rrCount * QR
            min = min(cand, min)
        print(min)
