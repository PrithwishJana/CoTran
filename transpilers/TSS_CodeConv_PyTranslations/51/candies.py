class candies:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        t = in_.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            a = in_.nextInt()
            x = [0 for _ in range(a)]
            for i in range(0, a):
                x [i] = in_.nextInt()
            x.sort()
            s = 0
            for i in range(0, a):
                s += abs(x [i] - x [0])
            print(s)
        t -= 1
