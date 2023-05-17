import math

class sub:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        num = in_.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (num -- > 0)
        while num  > 0:
            num -= 1
            a = in_.nextInt()
            b = in_.nextInt()
            res = 0
            while a != 0 and b != 0:
                if a >= b:
                    res += math.trunc(a / float(b))
                    a = math.fmod(a, b)
                else:
                    res += math.trunc(b / float(a))
                    b = math.fmod(b, a)
            print(res)
        num -= 1
