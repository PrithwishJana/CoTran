import math

class SortExample:
    @staticmethod
    def mySort(arr):
        n = len(arr)
        Arrays.sort(arr, 0, math.trunc(n / float(2)))
        Arrays.sort(arr, math.trunc(n / float(2)), n, Collections.reverseOrder())
    @staticmethod
    def main(args):
        arr = [5, 4, 6, 2, 1, 3, 8, 9, 7]
        SortExample.mySort(arr)
        print("Modified Array : {0}".format(Arrays.toString(arr)), end = '')
