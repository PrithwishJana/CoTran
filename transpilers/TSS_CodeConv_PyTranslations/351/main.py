import math

class main:
    @staticmethod
    def count(num):
        sum = 0
        while num > 0:
            sum += math.fmod(num, 10)
            num = math.trunc(num / float(10))
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = java.util.Scanner(System.in)
        k = 0
        i = 1
        mo = 19
        k = in_.nextInt()
        while i != k:
            mo += 1
            if 10 == main.count(mo):
                i += 1
        print(mo)
