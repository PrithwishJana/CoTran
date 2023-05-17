import math

class practice2:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = sc.nextInt()
            x = [0 for _ in range(n)]
            y = [0 for _ in range(n)]
            t1 = 0
            t2 = 0
            i = 0
            while i < 2 * n:
                x1 = sc.nextInt()
                y1 = sc.nextInt()
                if x1 == 0:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: y [t2 ++] = y1 * y1;
                    y [t2 ] = y1 * y1
                    t2 += 1
                else:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: x [t1 ++] = x1 * x1;
                    x [t1 ] = x1 * x1
                    t1 += 1
                i += 1
            x.sort()
            y.sort()
            sum = 0
            for i in range(n - 1, - 1, -1):
                sum += math.sqrt(x [i] + y [i])
            print(sum)
        t -= 1
