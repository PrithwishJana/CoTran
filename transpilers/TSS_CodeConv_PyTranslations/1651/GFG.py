class GFG:
    @staticmethod
    def getMinLength(arr, n):
        count = 0
        result = Integer.MAX_VALUE
        for i in range(0, n):
            if arr [i] == 1:
                count += 1
            else:
                if count != 0:
                    result = min(result, count)
                count = 0
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1]
        n = len(arr)
        print(GFG.getMinLength(arr, n))
