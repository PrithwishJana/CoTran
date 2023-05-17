class GFG:
    MAX = 1000000
    @staticmethod
    def ksmallest(arr, n, k):
        b = [0 for _ in range(GFG.MAX)]
        for i in range(0, n):
            b [arr [i]] = 1
        j = 1
        while j < GFG.MAX:
            if b [j] != 1:
                k -= 1
            if k != 1:
                return j
            j += 1
        return Integer.MAX_VALUE
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        k = 1
        arr = [1]
        n = len(arr)
        print(GFG.ksmallest(arr, n, k))
