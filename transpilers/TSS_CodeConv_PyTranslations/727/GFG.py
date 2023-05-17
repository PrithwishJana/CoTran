import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(arr, x, n):
        sum = 0
        for i in range(0, n):
            y = math.sqrt(arr [i])
            if math.floor(y) == math.ceil(y):
                sum += arr [i]
        if math.fmod(sum, x) == 0:
            return True
        else:
            return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 4, 9, 10]
        n = len(arr)
        x = 13
        if GFG.check(arr, x, n):
            print("Yes")
        else:
            print("No")
