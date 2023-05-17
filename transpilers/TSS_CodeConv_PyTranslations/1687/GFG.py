import math

class GFG:
    @staticmethod
    def modularSum(arr, n, m):
        if n > m:
            return True
        DP = [False for _ in range(m)]
        Arrays.fill(DP, False)
        for i in range(0, n):
            if DP [0]:
                return True
            temp = [False for _ in range(m)]
            Arrays.fill(temp, False)
            for j in range(0, m):
                if DP [j] == True:
                    if DP [math.fmod((j + arr [i]), m)] == False:
                        temp [math.fmod((j + arr [i]), m)] = True
            for j in range(0, m):
                if temp [j]:
                    DP [j] = True
            DP [math.fmod(arr [i], m)] = True
        return DP [0]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        arr = [1, 7]
        n = len(arr)
        m = 5
        if GFG.modularSum(arr, n, m):
            print("YES\n", end = '')
        else:
            print("NO\n", end = '')
