class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def bit(n):
        count = 0
        while n > 0:
            count += 1
            n = n & (n - 1)
        return count
    @staticmethod
    def maxSumOfBits(arr, n):
        for i in range(0, n):
            arr [i] = GFG.bit(arr [i])
        incl = arr [0]
        excl = 0
        excl_new = 0
        for i in range(1, n):
            excl_new = incl if (incl > excl) else excl
            incl = excl + arr [i]
            excl = excl_new
        return (incl if (incl > excl) else excl)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 4, 5, 6, 7, 20, 25]
        n = len(arr)
        print(GFG.maxSumOfBits(arr, n), end = '')
