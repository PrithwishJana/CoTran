import math

class GFG:
    @staticmethod
    def countDivisbleby4(s):
        n = len(s)
        count = 0
        for i in range(0, n):
            if s[i] == '4' or s[i] == '8' or s[i] == '0':
                count += 1
        i = 0
        while i < n - 1:
            h = (s[i] - '0') * 10 + (s[i + 1] - '0')
            if math.fmod(h, 4) == 0:
                count = count + i + 1
            i += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "124"
        print(GFG.countDivisbleby4(s))
