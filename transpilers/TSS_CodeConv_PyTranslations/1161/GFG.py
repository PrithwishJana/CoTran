class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def kthSmallest(arr, k):
        arr.sort()
        return arr [k - 1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [12, 3, 5, 7, 19]
        k = 2
        print("K'th smallest element is " + str(GFG.kthSmallest(arr, k)), end = '')
