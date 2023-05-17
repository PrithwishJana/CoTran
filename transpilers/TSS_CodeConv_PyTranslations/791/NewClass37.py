import math

class NewClass37:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        t = in_.nextInt()
        p = 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = in_.nextInt()
            count = 0
            x = n
            if n < 10:
                print(n)
                continue
            while x > 0:
                count += 1
                x = math.trunc(x / float(10))
            first = 0
            while count > 0:
                first = first * 10 + 1
                count -= 1
            sum = 0
            if first <= n:
                sum += math.trunc(n / float(first))
            first = math.trunc(first / float(10))
            while first > 0:
                sum += 9
                first = math.trunc(first / float(10))
            print(sum)
        t -= 1
