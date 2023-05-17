import math

class Test:
    arr = [1, 5, 7, - 1, 5]
    @staticmethod
    def getPairsCount(n, sum):
        hm = {}
        for i in range(0, n):
            if  Test.arr [i] not in hm.keys():
                hm[Test.arr [i]] = 0
            hm[Test.arr [i]] = hm[Test.arr [i]] + 1
        twice_count = 0
        for i in range(0, n):
            if hm[sum - Test.arr [i]] is not None:
                twice_count += hm[sum - Test.arr [i]]
            if sum - Test.arr [i] == Test.arr [i]:
                twice_count -= 1
        return math.trunc(twice_count / float(2))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sum = 6
        print("Count of pairs is " + str(Test.getPairsCount(len(Test.arr), sum)))
