import math

class GFG:
    @staticmethod
    def countEvenOdd(n):
        even_count = 0
        odd_count = 0
        while n > 0:
            rem = math.fmod(n, 10)
            if math.fmod(rem, 2) == 0:
                even_count += 1
            else:
                odd_count += 1
            n = math.trunc(n / float(10))
        print("Even count : " + str(even_count))
        print("Odd count : " + str(odd_count))
        if math.fmod(even_count, 2) == 0 and math.fmod(odd_count, 2) != 0:
            return 1
        else:
            return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 0
        n = 2335453
        t = GFG.countEvenOdd(n)
        if t == 1:
            print("YES")
        else:
            print("NO")
