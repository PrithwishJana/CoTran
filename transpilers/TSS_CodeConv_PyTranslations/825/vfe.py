import math

class vfe:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = Scanner(System.in)
        t = in_.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = in_.nextInt()
            if math.fmod(360, (180 - n)) == 0:
                print("YES")
            else:
                print("NO")
        t -= 1
