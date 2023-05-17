class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def ReplaceElements(arr, n):
        if n <= 1:
            return
        prev = arr [0]
        arr [0] = arr [0] ^ arr [1]
        i = 1
        while i < n - 1:
            curr = arr [i]
            arr [i] = prev ^ arr [i + 1]
            prev = curr
            i += 1
        arr [n - 1] = prev ^ arr [n - 1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 4, 5, 6]
        n = len(arr)
        GFG.ReplaceElements(arr, n)
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
