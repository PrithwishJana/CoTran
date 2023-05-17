class GFG:
    @staticmethod
    def getElements(a, arr, n):
        elements = [0 for _ in range(n + 1)]
        elements [0] = a
        for i in range(0, n):
            elements [i + 1] = arr [i] ^ elements [i]
        i = 0
        while i < n + 1:
            print(str(elements [i]) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [13, 2, 6, 1]
        n = len(arr)
        a = 5
        GFG.getElements(a, arr, n)
