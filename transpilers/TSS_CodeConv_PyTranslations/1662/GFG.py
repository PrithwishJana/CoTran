class GFG:
    @staticmethod
    def difference(arr, n):
        largest = arr [0]
        i = 0
        for i in range(0, n):
            if largest < arr [i]:
                largest = arr [i]
        for i in range(0, n):
            arr [i] = largest - arr [i]
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 5, 9, 3, 2]
        n = len(arr)
        GFG.difference(arr, n)
