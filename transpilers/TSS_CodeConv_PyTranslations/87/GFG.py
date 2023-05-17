class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def rearrange(arr, n):
        j = 0
        temp = 0
        for i in range(0, n):
            if arr [i] < 0:
                if i != j:
                    temp = arr [i]
                    arr [i] = arr [j]
                    arr [j] = temp
                j += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [- 1, 2, - 3, 4, 5, 6, - 7, 8, 9]
        n = len(arr)
        GFG.rearrange(arr, n)
        print(Arrays.toString(arr))
