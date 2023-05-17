class c:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        t = 0
        j = 0
        i = 0
        n = 0
        p1 = 0
        p2 = 0
        c = 0
        p = 0
        t = sc.nextInt()
        for j in range(1, t + 1):
            n = sc.nextInt()
            p = [0 for _ in range(n + 5)]
            for i in range(0, n):
                p [sc.nextInt()] = i
            p1 = p2 = p [1]
            print(1, end = '')
            for i in range(2, n + 1):
                c = p [i]
                if c > p2:
                    p2 = c
                elif c < p1:
                    p1 = c
                if (p2 - p1) == i - 1:
                    print(1, end = '')
                else:
                    print(0, end = '')
            print()
