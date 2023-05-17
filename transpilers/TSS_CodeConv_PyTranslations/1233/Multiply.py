import math

class Multiply:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            a = sc.nextInt()
            two = 0
            three = 0
            while math.fmod(a, 2) == 0:
                a = math.trunc(a / float(2))
                two += 1
            while math.fmod(a, 3) == 0:
                a = math.trunc(a / float(3))
                three += 1
            if a == 1:
                if three >= two:
                    temp = two
                    three -= two
                    temp += three * 2
                    print(temp)
                else:
                    print("-1")
            else:
                print("-1")
        t -= 1
