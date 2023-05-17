class AA:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
        for i in range(0, t):
            k = sc.nextLong()
            x = sc.nextInt()
            f = k * 9
            for y in range(x, 9):
                f -= 1
            print(f)
