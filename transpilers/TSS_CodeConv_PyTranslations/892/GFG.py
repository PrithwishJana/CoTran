import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findNth(n):
        count = 0
        curr = 1
        while True:
            sum = 0
            x = curr
            while x > 0:
                sum = sum + math.fmod(x, 10)
                x = math.trunc(x / float(10))
            if sum == 10:
                count += 1
            if count == n:
                return curr
            curr += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(GFG.findNth(5), end = '')
