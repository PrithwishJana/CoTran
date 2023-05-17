class GFG:
    @staticmethod
    def findMinEqualSums(a, N):
        sum = 0
        for i in range(0, N):
            sum += a [i]
        sum1 = 0
        sum2 = 0
        min = Integer.MAX_VALUE
        for i in range(0, N):
            sum1 += a [i]
            sum2 = sum - sum1
            if abs(sum1 - sum2) < min:
                min = abs(sum1 - sum2)
            if min == 0:
                break
        return min
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [3, 2, 1, 5, 7, 8]
        N = len(a)
        print(GFG.findMinEqualSums(a, N))
