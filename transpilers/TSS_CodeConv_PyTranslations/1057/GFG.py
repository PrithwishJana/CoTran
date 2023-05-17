import math

class GFG:
    @staticmethod
    def countMaxContiguous(arr, n):
        current_max = 0
        max_so_far = 0
        for i in range(0, n):
            if math.fmod(arr [i], 2) != 0:
                current_max = 0
            else:
                current_max += 1
                max_so_far = max(current_max, max_so_far)
        return max_so_far
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 0, 2, 4, 3, 8, 9]
        n = len(arr)
        print(GFG.countMaxContiguous(arr, n))
