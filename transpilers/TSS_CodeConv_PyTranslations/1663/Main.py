import math

class Count:
    @staticmethod
    def countKdivPairs(A, n, K):
        freq = [0 for _ in range(K)]
        for i in range(0, n):
            freq [math.fmod(A [i], K)] += 1
        sum = math.trunc(freq [0] * (freq [0] - 1) / float(2))
        i = 1
        while i <= math.trunc(K / float(2)) and i != (K - i):
            sum += freq [i] * freq [K - i]
            i += 1
        if math.fmod(K, 2) == 0:
            sum += (math.trunc(freq [math.trunc(K / float(2))] * (freq [math.trunc(K / float(2))] - 1) / float(2)))
        return sum
    @staticmethod
    def main(args):
        A = [2, 2, 1, 7, 5, 3]
        n = 6
        K = 4
        print(Count.countKdivPairs(A, n, K), end = '')
