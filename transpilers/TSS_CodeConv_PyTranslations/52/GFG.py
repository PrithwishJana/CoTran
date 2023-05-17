class GFG:
    @staticmethod
    def printKDistinct(arr, n, k):
        h = {}
        for i in range(0, n):
            if arr [i] in h.keys():
                h[arr [i]] = h[arr [i]] + 1
            else:
                h[arr [i]] = 1
        if len(h) < k:
            return - 1
        dist_count = 0
        for i in range(0, n):
            if h[arr [i]] == 1:
                dist_count += 1
            if dist_count == k:
                return arr [i]
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        ar = [1, 2, 1, 3, 4, 2]
        n = len(ar)
        print(GFG.printKDistinct(ar, n, 2))
