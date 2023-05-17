import math

class GFG:
    @staticmethod
    def MinStep(a, n):
        positive = 0
        negative = 0
        zero = 0
        step = 0
        for i in range(0, n):
            if a [i] == 0:
                zero += 1
            elif a [i] < 0:
                negative += 1
                step = step + (- 1 - a [i])
            else:
                positive += 1
                step = step + (a [i] - 1)
        if math.fmod(negative, 2) == 0:
            step = step + zero
        else:
            if zero > 0:
                step = step + zero
            else:
                step = step + 2
        return step
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [0, - 2, - 1, - 3, 4]
        n = len(a)
        print(GFG.MinStep(a, n))
