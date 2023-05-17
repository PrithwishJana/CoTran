class GFG:
    @staticmethod
    def getmax(arr, n, x):
        s = 0
        for i in range(0, n):
            s = s + arr [i]
        print(min(s, x))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 4]
        x = 5
        arr_size = len(arr)
        GFG.getmax(arr, arr_size, x)
