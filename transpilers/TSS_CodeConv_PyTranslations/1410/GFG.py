class GFG:
    @staticmethod
    def Mean(arr, n):
        sum = 0
        for i in range(0, n):
            sum = sum + arr [i]
        return sum / n
    @staticmethod
    def meanAbsDevtion(arr, n):
        absSum = 0
        for i in range(0, n):
            absSum = absSum + abs(arr [i] - GFG.Mean(arr, n))
        return absSum / n
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 15, 15, 17, 18, 21]
        n = len(arr)
        print(GFG.meanAbsDevtion(arr, n))
