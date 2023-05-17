class league:
    def solve(self, in_, out):
        n = in_.nextInt()
        num = 0
        a = [0 for _ in range(1000001)]
        start = 0
        for i in range(1, n + 1):
            num += in_.nextInt()
            for j in range(start, num):
                a [j] = i
            start = num
        m = in_.nextInt()
        for i in range(0, m):
            print(a [in_.nextInt() - 1], end = '')
            print()
    def run(self):
        with java.util.Scanner(System.in) as in_, PrintWriter(System.out) as out:
            self.solve(in_, out)
    @staticmethod
    def main(args):
        (league()).run()
