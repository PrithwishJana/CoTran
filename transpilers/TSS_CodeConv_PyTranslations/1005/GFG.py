class GFG:
    @staticmethod
    def findMaximumNum(arr, n):
        for i in range(n, 0, -1):
            count = 0
            for j in range(0, n):
                if i <= arr [j]:
                    count += 1
            if count >= i:
                return i
        return 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 8, 10]
        n = len(arr)
        print(GFG.findMaximumNum(arr, n))
