class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countSetBits(n):
        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count
    @staticmethod
    def pairs(arr, n, k):
        count = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                sum = GFG.countSetBits(arr [i]) + GFG.countSetBits(arr [j])
                if sum == k:
                    count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 4
        print(GFG.pairs(arr, n, k))
