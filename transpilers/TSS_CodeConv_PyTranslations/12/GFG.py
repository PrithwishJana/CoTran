class GFG:
    @staticmethod
    def checkIfSortRotated(arr, n):
        minEle = Integer.MAX_VALUE
        maxEle = Integer.MIN_VALUE
        minIndex = - 1
        for i in range(0, n):
            if arr [i] < minEle:
                minEle = arr [i]
                minIndex = i
        flag1 = True
        for i in range(1, minIndex):
            if arr [i] < arr [i - 1]:
                flag1 = False
                break
        flag2 = True
        for i in range(minIndex + 1, n):
            if arr [i] < arr [i - 1]:
                flag2 = False
                break
        if minIndex == 0:
            print("NO", end = '')
            return
        if flag1 and flag2 and (arr [n - 1] < arr [minIndex - 1]):
            print("YES")
        else:
            print("NO", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 4, 5, 1, 2]
        n = len(arr)
        GFG.checkIfSortRotated(arr, n)
