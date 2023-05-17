import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(k):
        if k <= 1:
            return False
        for i in range(2, k):
            if math.fmod(k, i) == 0:
                return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(num, k):
        flag = 1
        for i in range(2, k):
            if math.fmod(num, i) == 0:
                flag = 0
        if flag == 1:
            if math.fmod(num, k) == 0:
                return 1
            else:
                return 0
        else:
            return 0
    @staticmethod
    def findCount(a, b, k):
        count = 0
        if not GFG.isPrime(k):
            return 0
        else:
            ans = 0
            for i in range(a, b + 1):
                ans = GFG.check(i, k)
                if ans == 1:
                    count += 1
                else:
                    continue
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 2020
        b = 6300
        k = 29
        print(GFG.findCount(a, b, k))
