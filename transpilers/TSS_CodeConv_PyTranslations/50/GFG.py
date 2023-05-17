class GFG:
    @staticmethod
    def arraySortedOrNot(arr, n):
        if n == 0 or n == 1:
            return True
        for i in range(1, n):
            if arr [i - 1] > arr [i]:
                return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [20, 23, 23, 45, 78, 88]
        n = len(arr)
        if GFG.arraySortedOrNot(arr, n):
            print("Yes\n", end = '')
        else:
            print("No\n", end = '')
