import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(s):
        freq = [0 for _ in range(10)]
        r = 0
        i = 0
        for i in range(0, 10):
            freq [i] = 0
        while s != 0:
            r = math.fmod(s, 10)
            s = int((math.trunc(s / float(10))))
            freq [r] += 1
        xor__ = 0
        for i in range(0, 10):
            xor__ = xor__ ^ freq [i]
            if xor__ == 0:
                return True
            else:
                return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = 122233
        if GFG.check(s):
            print("Yes")
        else:
            print("No")
