class test247:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        t = in_.nextInt()
        for j in range(0, t):
            n = in_.nextInt()
            a = [0 for _ in range(n)]
            max = 0
            for i in range(0, n):
                a [i] = in_.nextLong()
            if n == 2:
                max = a [0] * a [1]
            i = 1
            while i < n - 1:
                if a [i - 1] > a [i + 1]:
                    if a [i] * a [i - 1] > max:
                        max = a [i] * a [i - 1]
                else:
                    if a [i] * a [i + 1] > max:
                        max = a [i] * a [i + 1]
                i += 1
            print(max)
        in_.close()
