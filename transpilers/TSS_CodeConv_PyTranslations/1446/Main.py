import math

class solution:
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return solution.gcd(b, math.fmod(a, b))
    @staticmethod
    def lcmOfArray(arr, n):
        if n < 1:
            return 0
        lcm = arr [0]
        for i in range(1, n):
            lcm = math.trunc((lcm * arr [i]) / float(solution.gcd(lcm, arr [i])))
        return lcm
    @staticmethod
    def minPerfectSquare(arr, n):
        minPerfectSq = 0
        lcm = solution.lcmOfArray(arr, n)
        minPerfectSq = int(lcm)
        cnt = 0
        while lcm > 1 and math.fmod(lcm, 2) == 0:
            cnt += 1
            lcm = math.trunc(lcm / float(2))
        if math.fmod(cnt, 2) != 0:
            minPerfectSq *= 2
        i = 3
        while lcm > 1:
            cnt = 0
            while math.fmod(lcm, i) == 0:
                cnt += 1
                lcm = math.trunc(lcm / float(i))
            if math.fmod(cnt, 2) != 0:
                minPerfectSq *= i
            i += 2
        return minPerfectSq
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 4, 5, 7]
        n = len(arr)
        print(solution.minPerfectSquare(arr, n))
