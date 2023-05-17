import math

class GFG:
    @staticmethod
    def canBeEqual(a, b, c, k):
        arr = [0 for _ in range(3)]
        arr [0] = a
        arr [1] = b
        arr [2] = c
        Arrays.sort(arr)
        diff = 2 * arr [2] - arr [1] - arr [0]
        k = k - diff
        if k < 0 or math.fmod(k, 3) != 0:
            return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a1 = 6
        b1 = 3
        c1 = 2
        k1 = 7
        if GFG.canBeEqual(a1, b1, c1, k1):
            print("Yes")
        else:
            print("No")
