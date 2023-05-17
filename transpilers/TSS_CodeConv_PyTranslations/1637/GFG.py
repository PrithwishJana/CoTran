import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(mid, array, n, K):
        count = 0
        sum = 0
        for i in range(0, n):
            if array [i] > mid:
                return False
            sum += array [i]
            if sum > mid:
                count += 1
                sum = array [i]
        count += 1
        if count <= K:
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(array, n, K):
        start = 1
        end = 0
        for i in range(0, n):
            end += array [i]
        answer = 0
        while start <= end:
            mid = math.trunc((start + end) / float(2))
            if GFG.check(mid, array, n, K):
                answer = mid
                end = mid - 1
            else:
                start = mid + 1
        return answer
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        array = [1, 2, 3, 4]
        n = len(array)
        K = 3
        print(GFG.solve(array, n, K))
