import math

class GFG:
    @staticmethod
    def find_count(arr):
        ans = 0
        for i in arr:
            x = Integer.bitCount(i)
            if math.fmod(i, x) == 0:
                ans += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 4, 5, 6]
        print(GFG.find_count(arr), end = '')
