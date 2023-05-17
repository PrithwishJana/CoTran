import math

class Test:
    @staticmethod
    def subsetPairNotDivisibleByK(arr, N, K):
        f = [0 for _ in range(K)]
        Arrays.fill(f, 0)
        for i in range(0, N):
            f [math.fmod(arr [i], K)] += 1
        if math.fmod(K, 2) == 0:
            f [math.trunc(K / float(2))] = min(f [math.trunc(K / float(2))], 1)
        res = min(f [0], 1)
        i = 1
        while i <= math.trunc(K / float(2)):
            res += max(f [i], f [K - i])
            i += 1
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 7, 2, 9, 1]
        N = len(arr)
        K = 3
        print(Test.subsetPairNotDivisibleByK(arr, N, K))
