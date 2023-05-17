import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPairs(n):
        num = ((math.trunc(n / float(2))) + 1)
        max = math.fmod(n, num)
        count = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                val = math.fmod((math.fmod((math.fmod(n, i)), j)), n)
                if val == max:
                    count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        print(GFG.countPairs(n))
