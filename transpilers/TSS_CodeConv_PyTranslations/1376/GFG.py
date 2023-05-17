import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getCount(v, n):
        Arrays.sort(v)
        cnt = 0
        for i in range(0, n):
            tmp = n - 1 - GFG.upperBound(v, n, v [i] - 1)
            if tmp == v [i]:
                cnt += 1
        return cnt
    @staticmethod
    def upperBound(array, length, value):
        low = 0
        high = length
        while low < high:
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final int mid = (low + high) / 2;
            mid = math.trunc((low + high) / float(2))
            if value >= array [mid]:
                low = mid + 1
            else:
                high = mid
        return low
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        v = [1, 2, 3, 4]
        print(GFG.getCount(v, n))
