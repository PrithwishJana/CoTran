import math

class B940:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        N = in_.nextInt()
        K = in_.nextInt()
        A = in_.nextInt()
        B = in_.nextInt()
        cost = 0
        while N != 1:
            if N < K:
                cost += (N - 1) * A
                break
            r = math.fmod(N, K)
            cost += r * A
            N -= r
            if B >= (N - math.trunc(N / float(K))) * A:
                cost += (N - 1) * A
                break
            cost += B
            N = math.trunc(N / float(K))
        print(cost)
