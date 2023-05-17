import math

class GFG:
    @staticmethod
    def countNumbersWith4(n):
        if n < 4:
            return 0
        d = int(math.log10(n))
        a = [0 for _ in range(d + 2)]
        a [0] = 0
        a [1] = 1
        for i in range(2, d + 1):
            a [i] = a [i - 1] * 9 + int(math.ceil(10 ** (i - 1)))
        p = int(math.ceil(10 ** d))
        msd = math.trunc(n / float(p))
        if msd == 4:
            return (msd) * a [d] + (math.fmod(n, p)) + 1
        if msd > 4:
            return (msd - 1) * a [d] + p + GFG.countNumbersWith4(math.fmod(n, p))
        return (msd) * a [d] + GFG.countNumbersWith4(math.fmod(n, p))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 328
        print("Count of numbers from 1 to " + str(n) + " that have 4 as a digit is " + str(GFG.countNumbersWith4(n)))
