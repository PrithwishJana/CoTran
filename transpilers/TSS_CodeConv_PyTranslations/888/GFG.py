import math

class GFG:
    @staticmethod
    def valueofX(ar, n):
        sum = 0
        for i in range(0, n):
            sum = sum + ar [i]
        if math.fmod(sum, n) == 0:
            return math.trunc(sum / float(n))
        else:
            A = math.trunc(sum / float(n))
            B = math.trunc(sum / float(n)) + 1
            ValueA = 0
            ValueB = 0
            for i in range(0, n):
                ValueA += (ar [i] - A) * (ar [i] - A)
                ValueB += (ar [i] - B) * (ar [i] - B)
            if ValueA < ValueB:
                return A
            else:
                return B
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 7
        arr = [6, 9, 1, 6, 1, 3, 7]
        print(GFG.valueofX(arr, n))
