class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSum(arr, n):
        arr.sort()
        sum = arr [0]
        i = 0
        while i < n - 1:
            if arr [i] != arr [i + 1]:
                sum = sum + arr [i + 1]
            i += 1
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 1, 1, 4, 5, 6]
        n = len(arr)
        print(GFG.findSum(arr, n))
