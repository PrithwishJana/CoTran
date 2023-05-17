class GFG:
    @staticmethod
    def findMaxDiff(arr, n):
        if n < 2:
            print("Invalid ")
            return 0
        min_val = Integer.MAX_VALUE
        max_val = Integer.MIN_VALUE
        for i in range(0, n):
            if (arr [i] - i) > max_val:
                max_val = arr [i] - i
            if (arr [i] - i) < min_val:
                min_val = arr [i] - i
        return (max_val - min_val)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [9, 15, 4, 12, 13]
        n = len(arr)
        print(GFG.findMaxDiff(arr, n))
