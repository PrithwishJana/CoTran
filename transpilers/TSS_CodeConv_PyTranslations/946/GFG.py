import math

class GFG:
    @staticmethod
    def findPairs(arr, n):
        cntEven = 0
        cntOdd = 0
        for i in range(0, n):
            if math.fmod(arr [i], 2) == 0:
                cntEven += 1
            else:
                cntOdd += 1
        evenPairs = 0
        evenPairs += (math.trunc((cntEven * (cntEven - 1)) / float(2)))
        evenPairs += (math.trunc((cntOdd * (cntOdd - 1)) / float(2)))
        oddPairs = 0
        oddPairs += (cntEven * cntOdd)
        print("Odd pairs = " + str(oddPairs))
        print("Even pairs = " + str(evenPairs))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        GFG.findPairs(arr, n)
