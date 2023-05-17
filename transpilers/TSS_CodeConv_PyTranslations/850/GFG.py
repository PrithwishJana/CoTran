import math

class GFG:
    @staticmethod
    def prime(n):
        i = 2
        while i * i <= n:
            if math.fmod(n, i) == 0:
                return False
            i += 1
        return True
    @staticmethod
    def thirdNumber(a, b):
        sum = 0
        temp = 0
        sum = a + b
        temp = 1
        if sum == 0:
            temp = 2
        while not GFG.prime(sum + temp):
            temp += 2
        print(temp, end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arr):
        a = 3
        b = 5
        GFG.thirdNumber(a, b)
