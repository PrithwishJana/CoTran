import math

class cfg:
    @staticmethod
    def subarrayCount(arr, n):
        result = 0
        fast = 0
        slow = 0
        for i in range(1, n):
            if arr [i] - arr [i - 1] == 1:
                fast += 1
            else:
                len = fast - slow + 1
                result += math.trunc(len * (len - 1) / float(2))
                fast = i
                slow = i
        if fast != slow:
            len = fast - slow + 1
            result += math.trunc(len * (len - 1) / float(2))
        return result
    @staticmethod
    def main(args):
        arr = [1, 2, 3, 5, 6, 7]
        n = len(arr)
        print(cfg.subarrayCount(arr, n))
