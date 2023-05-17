class Problem1:
    @staticmethod
    def main(args):
        s = java.util.Scanner(System.in)
        t = s.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            a = s.nextInt()
            b = s.nextInt()
            print(a + b)
        t -= 1
