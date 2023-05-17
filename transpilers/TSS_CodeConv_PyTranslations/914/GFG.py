import math

class GFG:
    @staticmethod
    def unsort(l, r, a, k):
        if k < 1 or l + 1 == r:
            return
        k -= 2
        mid = math.trunc((l + r) / float(2))
        temp = a [mid - 1]
        a [mid - 1] = a [mid]
        a [mid] = temp
        GFG.unsort(l, mid, a, k)
        GFG.unsort(mid, r, a, k)
    @staticmethod
    def arrayWithKCalls(n, k):
        if math.fmod(k, 2) == 0:
            print("NO SOLUTION", end = '')
            return
        a = [0 for _ in range(n + 1)]
        a [0] = 1
        for i in range(1, n):
            a [i] = i + 1
        k -= 1
        GFG.unsort(0, n, a, k)
        for i in range(0, n):
            print(str(a [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        k = 17
        GFG.arrayWithKCalls(n, k)
