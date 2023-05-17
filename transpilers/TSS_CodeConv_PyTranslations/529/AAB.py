class AAB:
    @staticmethod
    def maxSumPair(arr1, n1, arr2, n2):
        max1 = Integer.MIN_VALUE
        max2 = Integer.MIN_VALUE
        for i in range(0, n1):
            if arr1 [i] > max1:
                max1 = arr1 [i]
        for i in range(0, n2):
            if arr2 [i] > max2:
                max2 = arr2 [i]
        return max1 + max2
    @staticmethod
    def main(args):
        arr1 = [10, 2, 3]
        arr2 = [3, 4, 7]
        n1 = len(arr1)
        n2 = len(arr2)
        print(AAB.maxSumPair(arr1, n1, arr2, n2))
