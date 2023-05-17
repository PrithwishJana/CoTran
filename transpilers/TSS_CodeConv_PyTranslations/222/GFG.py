import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return GFG.gcd(b, math.fmod(a, b))
    @staticmethod
    def lcmOfArray(arr, n):
        if n < 1:
            return 0
        lcm = arr [0]
        for i in range(1, n):
            lcm = math.trunc((lcm * arr [i]) / float(GFG.gcd(lcm, arr [i])))
        return lcm
    @staticmethod
    def minPerfectCube(arr, n):
        minPerfectCube = 0
        lcm = GFG.lcmOfArray(arr, n)
        minPerfectCube = lcm
        cnt = 0
        while lcm > 1 and math.fmod(lcm, 2) == 0:
            cnt += 1
            lcm = math.trunc(lcm / float(2))
        if math.fmod(cnt, 3) == 2:
            minPerfectCube *= 2
        elif math.fmod(cnt, 3) == 1:
            minPerfectCube *= 4
        i = 3
        while lcm > 1:
            cnt = 0
            while math.fmod(lcm, i) == 0:
                cnt += 1
                lcm = math.trunc(lcm / float(i))
            if math.fmod(cnt, 3) == 1:
                minPerfectCube *= i * i
            elif math.fmod(cnt, 3) == 2:
                minPerfectCube *= i
            i += 2
        return minPerfectCube
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 125, 14, 42, 100]
        n = len(arr)
        print(GFG.minPerfectCube(arr, n))
