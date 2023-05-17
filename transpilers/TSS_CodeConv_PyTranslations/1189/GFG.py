import math

class GFG:
    class primeFactorization:
        def __init__(self, countOfPf, primeFactor):
            #instance fields found by Java to Python Converter:
            self.countOfPf = 0
            self.primeFactor = 0

            self.countOfPf = countOfPf
            self.primeFactor = primeFactor
    @staticmethod
    def generateDivisors(curIndex, curDivisor, arr):
        if curIndex == len(arr):
            print(str(curDivisor) + " ", end = '')
            return
        i = 0
        while i <= arr[curIndex].countOfPf:
            GFG.generateDivisors(curIndex + 1, curDivisor, arr)
            curDivisor *= arr[curIndex].primeFactor
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findDivisors(n):
        arr = list  ()
        i = 2
        while i * i <= n:
            if math.fmod(n, i) == 0:
                count = 0
                while math.fmod(n, i) == 0:
                    n = math.trunc(n / float(i))
                    count += 1
                arr.append(primeFactorization(count, i))
            i += 1
        if n > 1:
            arr.append(primeFactorization(1, n))
        curIndex = 0
        curDivisor = 1
        GFG.generateDivisors(curIndex, curDivisor, arr)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        GFG.findDivisors(n)
