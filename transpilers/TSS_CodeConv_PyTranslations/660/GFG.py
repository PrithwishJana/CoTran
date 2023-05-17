class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxSum(a, n):
        a.sort()
        sum = 0
        i = 0
        while i < n - 1:
            sum += a [i]
            i += 2
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 3, 2, 1, 4, 5]
        n = len(arr)
        print(GFG.maxSum(arr, n))
