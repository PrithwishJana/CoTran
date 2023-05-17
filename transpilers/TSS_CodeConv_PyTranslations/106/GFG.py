class GFG:
    @staticmethod
    def LCIS(arr1, n, arr2, m):
        table = [0 for _ in range(m)]
        for j in range(0, m):
            table [j] = 0
        for i in range(0, n):
            current = 0
            for j in range(0, m):
                if arr1 [i] == arr2 [j]:
                    if current + 1 > table [j]:
                        table [j] = current + 1
                if arr1 [i] > arr2 [j]:
                    if table [j] > current:
                        current = table [j]
        result = 0
        for i in range(0, m):
            if table [i] > result:
                result = table [i]
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr1 = [3, 4, 9, 1]
        arr2 = [5, 3, 8, 9, 10, 2, 1]
        n = len(arr1)
        m = len(arr2)
        print("Length of LCIS is " + str(GFG.LCIS(arr1, n, arr2, m)))
