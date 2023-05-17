class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getCount(arr, n, num1, num2):
        i = 0
        for i in range(0, n):
            if arr [i] == num1:
                break
        if i >= n - 1:
            return 0
        j = 0
        j = n - 1
        while j >= i + 1:
            if arr [j] == num2:
                break
            j -= 1
        if j == i:
            return 0
        return (j - i - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 5, 7, 6, 4, 9, 12, 4, 8]
        n = len(arr)
        num1 = 5
        num2 = 4
        print(GFG.getCount(arr, n, num1, num2))
