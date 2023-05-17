class GFG:
    @staticmethod
    def printSmall(arr, asize, n):
        copy_arr = Arrays.copyOf(arr, asize)
        Arrays.sort(copy_arr)
        for i in range(0, asize):
            if Arrays.binarySearch(copy_arr, 0, n, arr [i]) > - 1:
                print(str(arr [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 5, 8, 9, 6, 7, 3, 4, 2, 0]
        asize = len(arr)
        n = 5
        GFG.printSmall(arr, asize, n)
