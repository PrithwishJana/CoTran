class A30:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        A = in_.nextInt()
        B = in_.nextInt()
        N = in_.nextInt()
        bigA = java.math.BigInteger.valueOf(A)
        bigB = java.math.BigInteger.valueOf(B)
        for x in range(- 1000, 1001):
            if java.math.BigInteger.valueOf(x).pow(N).multiply(bigA) is bigB:
                print(x)
                return
        print("No solution")
