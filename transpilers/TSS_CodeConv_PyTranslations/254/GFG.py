class GFG:
    @staticmethod
    def findCart(arr1, arr2, n, n1):
        for i in range(0, n):
            for j in range(0, n1):
                print("{" + str(arr1 [i]) + ", " + str(arr2 [j]) + "}, ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        n1 = len(arr1)
        n2 = len(arr2)
        GFG.findCart(arr1, arr2, n1, n2)
