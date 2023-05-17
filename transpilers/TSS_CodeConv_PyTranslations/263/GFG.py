import math

class GFG:
    @staticmethod
    def ansQueries(prefeven, prefodd, l, r):
        if math.fmod((r - l + 1), 2) == 0:
            print("0")
        else:
            if math.fmod(l, 2) == 0:
                print(prefeven [r] ^ prefeven [l - 1])
            else:
                print(prefodd [r] ^ prefodd [l - 1])
    @staticmethod
    def wrapper(arr, n, l, r, q):
        prefodd = [0 for _ in range(100)]
        prefeven = [0 for _ in range(100)]
        for i in range(1, n + 1):
            if math.fmod((i), 2) == 0:
                prefeven [i] = arr [i - 1] ^ prefeven [i - 1]
                prefodd [i] = prefodd [i - 1]
            else:
                prefeven [i] = prefeven [i - 1]
                prefodd [i] = prefodd [i - 1] ^ arr [i - 1]
        i = 0
        while i != q:
            GFG.ansQueries(prefeven, prefodd, l [i], r [i])
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        l = [1, 1, 2]
        r = [2, 3, 4]
        q = len(l)
        GFG.wrapper(arr, n, l, r, q)
