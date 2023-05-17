class GFG:
    @staticmethod
    def Swap(array, position1, position2):
        temp = array [position1]
        array [position1] = array [position2]
        array [position2] = temp
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def partition(arr, low, high):
        pivot = arr [high]
        i = (low - 1)
        j = low
        while j <= high - 1:
            if arr [j] <= pivot:
                i += 1
                GFG.Swap(arr, i, j)
            j += 1
        GFG.Swap(arr, i + 1, high)
        return (i + 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def quickSort(arr, low, high):
        if low < high:
            pi = GFG.partition(arr, low, high)
            GFG.quickSort(arr, low, pi - 1)
            GFG.quickSort(arr, pi + 1, high)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printArray(arr, size):
        i = 0
        for i in range(0, size):
            print(str(arr [i]) + " ", end = '')
        print()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 7, 8, 9, 1, 5]
        n = len(arr)
        GFG.quickSort(arr, 0, n - 1)
        print("Sorted array:")
        GFG.printArray(arr, n)
