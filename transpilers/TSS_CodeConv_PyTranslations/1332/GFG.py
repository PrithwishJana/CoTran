class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findElements(arr, n):
        for i in range(0, n):
            count = 0
            for j in range(0, n):
                if arr [j] > arr [i]:
                    count += 1
            if count >= 2:
                print(str(arr [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, - 6, 3, 5, 1]
        n = len(arr)
        GFG.findElements(arr, n)
