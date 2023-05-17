import math

class GFG:
    @staticmethod
    def Prime(n):
        if n == 1:
            return False
        i = 2
        while i * i <= n:
            if math.fmod(n, i) == 0:
                return False
            i += 1
        return True
    @staticmethod
    def checkSumPrime(str):
        summ = 0
        i = 1
        while i < len(str):
            summ += abs(str[i - 1] - str[i])
            i += 1
        if GFG.Prime(summ):
            return True
        else:
            return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        num = 142
        str = "142"
        if GFG.checkSumPrime(str):
            print("Prime")
        else:
            print("Not Prime")
