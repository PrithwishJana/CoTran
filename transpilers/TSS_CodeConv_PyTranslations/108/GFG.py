class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def partition(arr, low, high):
        pivot = arr [low]
        i = low - 1
        j = high + 1
        while True:
            loop_condition = True
            while loop_condition:
                i += 1
                loop_condition = arr [i] < pivot
            loop_condition = True
            while loop_condition:
                j -= 1
                loop_condition = arr [j] > pivot
            if i >= j:
                return j
            temp = arr [i]
            arr [i] = arr [j]
            arr [j] = temp
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def quickSort(arr, low, high):
        if low < high:
            pi = GFG.partition(arr, low, high)
            GFG.quickSort(arr, low, pi)
            GFG.quickSort(arr, pi + 1, high)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printArray(arr, n):
        for i in range(0, n):
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
