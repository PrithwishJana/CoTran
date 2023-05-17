import math

class GFG:
    @staticmethod
    def lastFiveDigits(n):
        n = (math.trunc(n / float(10000))) * 10000 + (math.fmod((math.trunc(n / float(100))), 10)) * 1000 + (math.fmod(n, 10)) * 100 + (math.fmod((math.trunc(n / float(10))), 10)) * 10 + math.fmod((math.trunc(n / float(1000))), 10)
        ans = 1
        for i in range(0, 5):
            ans *= n
            ans = math.fmod(ans, 100000)
        print(ans)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 12345
        GFG.lastFiveDigits(n)
