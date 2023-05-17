class GFG:
    @staticmethod
    def isPeak(arr, n, num, i, j):
        if i >= 0 and arr [i] > num:
            return False
        if j < n and arr [j] > num:
            return False
        return True
    @staticmethod
    def isTrough(arr, n, num, i, j):
        if i >= 0 and arr [i] < num:
            return False
        if j < n and arr [j] < num:
            return False
        return True
    @staticmethod
    def printPeaksTroughs(arr, n):
        print("Peaks : ", end = '')
        for i in range(0, n):
            if GFG.isPeak(arr, n, arr [i], i - 1, i + 1):
                print(str(arr [i]) + " ", end = '')
        print("")
        print("Troughs : ", end = '')
        for i in range(0, n):
            if GFG.isTrough(arr, n, arr [i], i - 1, i + 1):
                print(str(arr [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 10, 5, 7, 4, 3, 5]
        n = len(arr)
        GFG.printPeaksTroughs(arr, n)
