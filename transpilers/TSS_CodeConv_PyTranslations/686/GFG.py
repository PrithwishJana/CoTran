class GFG:
    @staticmethod
    def makearrayequal(arr, n):
        x = 0
        for i in range(0, n):
            x += (arr [i] & 1)
        print(min(x, n - x))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 3, 2, 1]
        n = len(arr)
        GFG.makearrayequal(arr, n)
