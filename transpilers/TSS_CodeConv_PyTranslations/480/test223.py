import math

class test223:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        t = in_.nextInt()
        for j in range(0, t):
            x = in_.nextInt()
            if x == 1:
                print("2")
            elif x == 2:
                print("1")
            elif math.fmod(x, 3) == 0:
                print(math.trunc(x / float(3)))
            else:
                print(math.trunc(x / float(3)) + 1)
        in_.close()
