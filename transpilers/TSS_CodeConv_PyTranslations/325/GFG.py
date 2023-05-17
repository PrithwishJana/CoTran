import math

class GFG:
    @staticmethod
    def findPairCount(N, K):
        count = 0
        rem = [0 for _ in range(K)]
        rem [0] = math.trunc(N / float(K))
        for i in range(1, K):
            rem [i] = math.trunc((N - i) / float(K)) + 1
        if math.fmod(K, 2) == 0:
            count += math.trunc((rem [0] * (rem [0] - 1)) / float(2))
            i = 1
            while i < math.trunc(K / float(2)):
                count += rem [i] * rem [K - i]
                i += 1
            count += math.trunc((rem [math.trunc(K / float(2))] * (rem [math.trunc(K / float(2))] - 1)) / float(2))
        else:
            count += math.trunc((rem [0] * (rem [0] - 1)) / float(2))
            i = 1
            while i <= math.trunc(K / float(2)):
                count += rem [i] * rem [K - i]
                i += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 10
        K = 4
        print(GFG.findPairCount(N, K))
