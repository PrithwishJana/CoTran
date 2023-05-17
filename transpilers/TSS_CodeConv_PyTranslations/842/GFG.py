class GFG:
    @staticmethod
    def originalArray(greater, n):
        temp = []
        for i in range(0, n + 1):
            temp.append(i)
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            k = n - greater [i] - i
            arr [i] = temp[k]
            temp.pop(k)
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        Arr = [6, 3, 2, 1, 0, 1, 0]
        n = len(Arr)
        GFG.originalArray(Arr, n)
