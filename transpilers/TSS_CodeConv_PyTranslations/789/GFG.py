import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPerfectSquare(x):
        sr = math.sqrt(x)
        return ((sr - math.floor(sr)) == 0)
    @staticmethod
    def isProduct(num):
        cnt = 0
        i = 2
        while cnt < 2 and i * i <= num:
            while math.fmod(num, i) == 0:
                num = math.trunc(num / float(i))
                cnt += 1
            i += 1
        if num > 1:
            cnt += 1
        return cnt == 2
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findNumbers(N):
        vec = list  ()
        for i in range(1, N + 1):
            if GFG.isProduct(i) and not GFG.isPerfectSquare(i):
                vec.append(i)
        itr = vec.iterator()
        while itr.hasNext():
            print(itr.next() + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 30
        GFG.findNumbers(N)
