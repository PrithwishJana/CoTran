class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def minSum(arr, n):
        sum = arr [0]
        prev = arr [0]
        for i in range(1, n):
            if arr [i] <= prev:
                prev = prev + 1
                sum = sum + prev
            else:
                sum = sum + arr [i]
                prev = arr [i]
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 2, 3, 5, 6]
        n = len(arr)
        print(GFG.minSum(arr, n))
