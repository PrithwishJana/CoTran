class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def search(arr, x):
        n = len(arr)
        for i in range(0, n):
            if arr [i] == x:
                return i
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 4, 10, 40]
        x = 10
        result = GFG.search(arr, x)
        if result == - 1:
            print("Element is not present in array", end = '')
        else:
            print("Element is present at index " + str(result), end = '')
