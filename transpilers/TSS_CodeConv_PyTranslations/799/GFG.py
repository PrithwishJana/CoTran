import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def find(arr, length, s):
        i = 1
        while i <= (2 ** length):
            sum = 0
            for j in range(0, length):
                if (math.fmod(((i >> j) & 1), 2)) == 1:
                    sum += arr [j]
            if sum == s:
                print("YES")
                return
            i += 1
        print("NO")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sum = 5
        array = [- 1, 2, 4, 121]
        length = len(array)
        GFG.find(array, length, sum)
