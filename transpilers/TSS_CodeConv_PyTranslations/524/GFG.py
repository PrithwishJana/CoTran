class GFG:
    @staticmethod
    def findEle(arr, n):
        sum = 0
        for i in range(0, n):
            sum += arr [i]
        for i in range(0, n):
            if arr [i] == sum - arr [i]:
                return arr [i]
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 6]
        n = len(arr)
        print(GFG.findEle(arr, n), end = '')
