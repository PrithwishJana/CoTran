class submitfinal:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
        while t != 0:
            n = sc.nextInt()
            x = 0
            y = 0
            temp1 = Integer.MIN_VALUE
            temp2 = Integer.MAX_VALUE
            for i in range(0, n):
                x = sc.nextInt()
                y = sc.nextInt()
                temp1 = max(temp1, x)
                temp2 = min(temp2, y)
            print(max(0, (temp1 - temp2)))
            t -= 1
