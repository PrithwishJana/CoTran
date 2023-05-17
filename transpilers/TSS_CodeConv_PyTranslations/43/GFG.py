class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printArray(N, arr):
        for i in range(0, N):
            print(str(arr [i]) + " ", end = '')
        print()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def replacedArray(N, arr):
        pos_sum = 0
        neg_sum = 0
        i = 0
        j = 0
        diff = 0
        for i in range(0, N):
            pos_sum = 0
            neg_sum = 0
            for j in range(i + 1, N):
                if arr [j] > 0:
                    pos_sum += arr [j]
                else:
                    neg_sum += arr [j]
            diff = abs(pos_sum) - abs(neg_sum)
            arr [i] = abs(diff)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 5
        arr = [1, - 1, 2, 3, - 2]
        GFG.replacedArray(N, arr)
        GFG.printArray(N, arr)
        N = 6
        arr1 = [- 3, - 4, - 2, 5, 1, - 2]
        GFG.replacedArray(N, arr1)
        GFG.printArray(N, arr1)
