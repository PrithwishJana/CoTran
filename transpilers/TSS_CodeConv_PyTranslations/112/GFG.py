import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printArray(N, SUM, K):
        minSum = math.trunc((N * (N + 1)) / float(2))
        maxSum = (N * K) - math.trunc((N * (N - 1)) / float(2))
        if minSum > SUM or maxSum < SUM:
            print("Not Possible")
            return
        arr = [0 for _ in range(N + 1)]
        for i in range(1, N + 1):
            arr [i] = i
        sum = minSum
        for i in range(N, 0, -1):
            x = sum + (K - i)
            if x < SUM:
                sum = sum + (K - i)
                arr [i] = K
                K -= 1
            else:
                arr [i] += (SUM - sum)
                sum = SUM
                break
        for i in range(1, N + 1):
            print(str(arr [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 3
        SUM = 15
        K = 8
        GFG.printArray(N, SUM, K)
