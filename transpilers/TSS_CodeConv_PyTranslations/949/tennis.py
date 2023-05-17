class tennis:
    @staticmethod
    def main(args):
        in_ = Scanner(System.in)
        sb = StringBuilder()
        res = 0
        cnt1 = 0
        cnt2 = 0
        n = in_.nextInt()
        m = in_.nextInt()
        z = in_.nextInt()
        for i in range(m, z + 1, m):
            for j in range(n, z + 1, n):
                if i == j:
                    res += 1
        print(res)
