import math

class NewClass27:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        t = in_.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            w = in_.nextInt()
            h = in_.nextInt()
            n = in_.nextInt()
            sheet = 1
            while math.fmod(w, 2) == 0:
                w = math.trunc(w / float(2))
                sheet *= 2
            while math.fmod(h, 2) == 0:
                h = math.trunc(h / float(2))
                sheet *= 2
            if sheet >= n:
                print("YES")
            else:
                print("NO")
        t -= 1
