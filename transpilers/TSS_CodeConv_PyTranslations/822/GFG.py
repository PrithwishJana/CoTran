import math

class GFG:
    @staticmethod
    def smallestPermute(n):
        res = ['\0' for _ in range(n + 1)]
        if math.fmod(n, 2) == 0:
            for i in range(0, n):
                if math.fmod(i, 2) == 0:
                    res [i] = chr((48 + i + 2))
                else:
                    res [i] = chr((48 + i))
        else:
            i = 0
            while i < n - 2:
                if math.fmod(i, 2) == 0:
                    res [i] = chr((48 + i + 2))
                else:
                    res [i] = chr((48 + i))
                i += 1
            res [n - 1] = chr((48 + n - 2))
            res [n - 2] = chr((48 + n))
            res [n - 3] = chr((48 + n - 1))
        res [n] = '\0'
        for i in range(0, n):
            print(res [i], end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 7
        GFG.smallestPermute(n)
