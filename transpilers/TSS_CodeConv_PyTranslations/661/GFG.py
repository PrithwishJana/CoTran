import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findAnswer(n, arr):
        Arrays.sort(arr)
        sum = 0
        i = 0
        while i < math.trunc(n / float(2)):
            sum += (arr [i] + arr [n - i - 1]) * (arr [i] + arr [n - i - 1])
            i += 1
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [53, 28, 143, 5]
        n = len(arr)
        print(GFG.findAnswer(n, arr))
