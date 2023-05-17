class a:
    @staticmethod
    def main(args):
        in_ = Scanner(System.in)
        n = in_.nextInt()
        a = [0 for _ in range(3)]
        a [0] = in_.nextInt()
        a [1] = in_.nextInt()
        a [2] = in_.nextInt()
        Arrays.sort(a)
        max = 0
        d = [0 for _ in range(n + 1)]
        Arrays.fill(d, - 500)
        d [0] = 0
        for i in range(0, n + 1):
            for j in range(0, 3):
                if i - a [j] >= 0 and d [i - a [j]] != - 1:
                    d [i] = max(d [i], d [i - a [j]] + 1)
        print(d [n])
