class D:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        T = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (T -- > 0)
        while T  > 0:
            T -= 1
            n = sc.nextInt()
            a = [0 for _ in range(n)]
            for i in range(0, n):
                a [i] = sc.nextInt()
            Arrays.sort(a)
            mini = 0
            ans = 0
            for i in range(1, n):
                diff = a [i] - a [i - 1]
                mini = mini + (- 1) * diff * i
                ans += mini
            print(ans + a [n - 1])
        T -= 1
