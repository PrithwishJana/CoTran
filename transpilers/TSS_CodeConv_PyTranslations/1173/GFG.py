import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSubsequence(arr, n):
        len = 1
        tmp = 0
        i = 0
        j = 0
        d = 0
        dp = [0 for _ in range(10)]
        cnt = [0 for _ in range(10)]
        locMax = 0
        tmp = arr [0]
        while tmp > 0:
            dp [math.fmod(tmp, 10)] = 1
            tmp = math.trunc(tmp / float(10))
        for i in range(1, n):
            tmp = arr [i]
            locMax = 1
            Arrays.fill(cnt, 0)
            while tmp > 0:
                cnt [math.fmod(tmp, 10)] = 1
                tmp = math.trunc(tmp / float(10))
            for d in range(0, 10):
                if cnt [d] == 1:
                    dp [d] += 1
                    locMax = max(locMax, dp [d])
            for d in range(0, 10):
                if cnt [d] == 1:
                    dp [d] = locMax
            len = max(len, locMax)
        return len
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 12, 44, 29, 33, 96, 89]
        n = len(arr)
        print(GFG.findSubsequence(arr, n), end = '')
