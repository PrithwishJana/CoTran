class GFG:
    @staticmethod
    def minDiff(arr, n, k):
        result = Integer.MAX_VALUE
        Arrays.sort(arr)
        i = 0
        while i <= n - k:
            result = min(result, arr [i + k - 1] - arr [i])
            i += 1
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 100, 300, 200, 1000, 20, 30]
        n = len(arr)
        k = 3
        print(GFG.minDiff(arr, n, k))
