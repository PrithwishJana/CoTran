class GFG:
    @staticmethod
    def command(arr, a, b):
        arr [a] ^= True
        arr [b + 1] ^= True
    @staticmethod
    def process(arr, n):
        for k in range(1, n + 1):
            arr [k] ^= arr [k - 1]
    @staticmethod
    def result(arr, n):
        for k in range(1, n + 1):
            if arr [k] == True:
                print("1" + " ", end = '')
            else:
                print("0" + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        m = 3
        arr = [False for _ in range(n + 2)]
        GFG.command(arr, 1, 5)
        GFG.command(arr, 2, 5)
        GFG.command(arr, 3, 5)
        GFG.process(arr, n)
        GFG.result(arr, n)
