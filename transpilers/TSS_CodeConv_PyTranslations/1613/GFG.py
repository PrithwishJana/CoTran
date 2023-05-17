class GFG:
    @staticmethod
    def minflip(arr1, arr2, arr3, p, q, n):
        flip = 0
        for i in range(0, n):
            if arr1 [i] > 0 ^ (arr2 [i] > 0) != (arr3 [i] > 0):
                flip += 1
        return flip if (flip <= p + q) else - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr1 = [1, 0, 1, 1, 1, 1, 1]
        arr2 = [0, 1, 1, 1, 1, 0, 0]
        arr3 = [1, 1, 1, 1, 0, 0, 1]
        n = len(arr1)
        p = 2
        q = 4
        print(GFG.minflip(arr1, arr2, arr3, p, q, n))
