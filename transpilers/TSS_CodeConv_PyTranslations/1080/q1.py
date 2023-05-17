class q1:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            a = 0
            b = 0
            c = 0
            d = 0
            a = sc.nextLong()
            b = sc.nextLong()
            c = sc.nextLong()
            d = sc.nextLong()
            res = max(c - 1, a - c) + max(d - 1, b - d)
            print(res)
        t -= 1
