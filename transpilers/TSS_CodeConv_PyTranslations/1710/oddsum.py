import math

class oddsum:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        t = in_.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            s = 0
            o = 0
            e = 0
            a = in_.nextInt()
            x = 0
            for i in range(0, a):
                x = in_.nextInt()
                s += x
                if math.fmod(x, 2) != 0:
                    o += 1
                else:
                    e += 1
            if math.fmod(s, 2) != 0:
                print("YES")
            else:
                if o >= 1 and e >= 1:
                    print("YES")
                else:
                    print("NO")
        t -= 1
