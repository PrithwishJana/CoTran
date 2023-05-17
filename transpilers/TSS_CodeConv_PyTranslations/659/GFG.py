class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxSum(arr, n):
        Arrays.sort(arr)
        sum = 0
        for i in range(0, n):
            sum += (arr [i] * i)
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 5, 6, 1]
        n = len(arr)
        print(GFG.maxSum(arr, n))
