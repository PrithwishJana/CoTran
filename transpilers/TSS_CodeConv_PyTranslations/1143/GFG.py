class GFG:
    @staticmethod
    def findEncryptedArray(arr, n):
        sum = 0
        for i in range(0, n):
            sum += arr [i]
        for i in range(0, n):
            print(sum - str(arr [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 1, 3, 2, 4]
        N = len(arr)
        GFG.findEncryptedArray(arr, N)
