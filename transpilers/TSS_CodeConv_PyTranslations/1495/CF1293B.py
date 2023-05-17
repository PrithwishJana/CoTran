class CF1293B:
    scanner = None
    @staticmethod
    def main(args):
        CF1293B.scanner = java.util.Scanner(System.in)
        n = CF1293B.scanner.nextInt()
        res = 0
        for i in range(0, n):
            res += (1.0 / float((n - i)))
        print(res)
