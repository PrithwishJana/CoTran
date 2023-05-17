class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def negProdSubArr(arr, n):
        positive = 1
        negative = 0
        for i in range(0, n):
            if arr [i] > 0:
                arr [i] = 1
            else:
                arr [i] = - 1
            if i > 0:
                arr [i] *= arr [i - 1]
            if arr [i] == 1:
                positive += 1
            else:
                negative += 1
        return (positive * negative)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, - 4, - 3, 2, - 5]
        n = len(arr)
        print(GFG.negProdSubArr(arr, n))
