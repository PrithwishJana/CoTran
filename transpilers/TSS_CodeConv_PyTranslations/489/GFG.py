class GFG:
    @staticmethod
    def count_greater(arr, n):
        min = Integer.MAX_VALUE
        counter = 0
        for i in range(n - 1, -1, -1):
            if arr [i] > min:
                counter += 1
            if arr [i] <= min:
                min = arr [i]
        return counter
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 2, 1, 2, 3, 4, 5]
        n = len(arr)
        print(GFG.count_greater(arr, n))
