import math

class TwoRegularPolygons:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = sc.nextInt()
            m = sc.nextInt()
            print("YES" if (math.fmod(n, m)) == 0 else "NO")
        t -= 1
