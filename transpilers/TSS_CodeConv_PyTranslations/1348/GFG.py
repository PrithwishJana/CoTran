import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countDigits(val, arr):
        while int(val) > 0:
            digit = math.fmod(int(val), 10)
            arr [int(digit)] += 1
            val = math.trunc(int(val) / float(10))
        return
    @staticmethod
    def countFrequency(x, n):
        freq_count = [0 for _ in range(10)]
        for i in range(1, n + 1):
            val = (float(x)) ** (float(i))
            GFG.countDigits(val, freq_count)
        for i in range(0, 10):
            print(str(freq_count [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 15
        n = 3
        GFG.countFrequency(x, n)
