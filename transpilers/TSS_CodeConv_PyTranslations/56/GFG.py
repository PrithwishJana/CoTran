class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countEleLessThanOrEqual(arr1, arr2, m, n):
        for i in range(0, m):
            count = 0
            for j in range(0, n):
                if arr2 [j] <= arr1 [i]:
                    count += 1
            print(str(count) + " ", end = '')
        return m
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr1 = [1, 2, 3, 4, 7, 9]
        arr2 = [0, 1, 2, 1, 1, 4]
        GFG.countEleLessThanOrEqual(arr1, arr2, len(arr1), len(arr2))
