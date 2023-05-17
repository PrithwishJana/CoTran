class GFG:
    @staticmethod
    def findMinDifference(arr, n):
        min = 0
        secondMin = 0
        max = 0
        secondMax = 0
        min = secondMax = arr [0] if (arr [0] < arr [1]) else arr [1]
        max = secondMin = arr [1] if (arr [0] < arr [1]) else arr [0]
        for i in range(2, n):
            if arr [i] > max:
                secondMax = max
                max = arr [i]
            elif arr [i] > secondMax:
                secondMax = arr [i]
            elif arr [i] < min:
                secondMin = min
                min = arr [i]
            elif arr [i] < secondMin:
                secondMin = arr [i]
        diff = min(max - secondMin, secondMax - min)
        return diff
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 4, 3, 4]
        n = len(arr)
        print(GFG.findMinDifference(arr, n))
