class GFG:
    @staticmethod
    def checkType(arr, n):
        if arr [0] <= arr [1] and arr [n - 2] <= arr [n - 1]:
            print("Increasing")
        elif arr [0] >= arr [1] and arr [n - 2] >= arr [n - 1]:
            print("Decreasing")
        elif arr [0] <= arr [1] and arr [n - 2] >= arr [n - 1]:
            print("Increasing then decreasing")
        else:
            print("Decreasing then increasing")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 4]
        n = len(arr)
        GFG.checkType(arr, n)
