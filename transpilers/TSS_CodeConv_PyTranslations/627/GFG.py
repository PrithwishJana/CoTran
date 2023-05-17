import math

class GFG:
    @staticmethod
    def isPerfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if math.fmod(n, i) == 0:
                if i * i != n:
                    sum = sum + i + math.trunc(n / float(i))
                else:
                    sum = sum + i
            i += 1
        if sum == n and n != 1:
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print("Below are all perfect numbers till 10000")
        for n in range(2, 10000):
            if GFG.isPerfect(n):
                print(str(n) + " is a perfect number")
