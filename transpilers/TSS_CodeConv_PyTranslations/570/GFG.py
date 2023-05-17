class GFG:
    @staticmethod
    def checkEVENodd(arr, n, l, r):
        if arr [r] == 1:
            print("odd")
        else:
            print("even")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 1, 0, 1]
        n = len(arr)
        GFG.checkEVENodd(arr, n, 1, 3)
