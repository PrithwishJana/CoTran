class GFG:
    MAX = 1000000
    @staticmethod
    def maximumOccurredElement(L, R, n):
        arr = [0 for _ in range(GFG.MAX)]
        maxi = - 1
        for i in range(0, n):
            arr [L [i]] += 1
            arr [R [i] + 1] -= 1
            if R [i] > maxi:
                maxi = R [i]
        msum = arr [0]
        ind = 0
        i = 1
        while i < maxi + 1:
            arr [i] += arr [i - 1]
            if msum < arr [i]:
                msum = arr [i]
                ind = i
            i += 1
        return ind
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        L = [1, 4, 9, 13, 21]
        R = [15, 8, 12, 20, 30]
        n = len(L)
        print(GFG.maximumOccurredElement(L, R, n))
