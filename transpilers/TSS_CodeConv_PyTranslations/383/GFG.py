import math

class GFG:
    @staticmethod
    def printSeriesSum(N):
        sum = 0
        a = 1
        cnt = 0
        flag = True
        sum += a
        while cnt < N:
            nextElement = 0
            if flag == True:
                nextElement = a * 2
                sum += nextElement
                flag = not flag
            else:
                nextElement = math.trunc(a * 3 / float(2))
                sum += nextElement
                flag = not flag
            a = nextElement
            cnt += 1
        print(sum)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 8
        GFG.printSeriesSum(N)
