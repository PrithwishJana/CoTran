class GFG:
    MAX = 50009
    @staticmethod
    def find_Indices(arr, n):
        sum = [0 for _ in range(GFG.MAX)]
        index_1 = 0
        index_2 = 0
        index_3 = 0
        index = 0
        k = 0
        i = 0
        i = 1
        k = 0
        while i <= n:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: sum [i] = sum [i - 1] + arr [k ++];
            sum [i] = sum [i - 1] + arr [k ]
            k += 1
            i += 1
        ans = - (1e15)
        index_1 = index_2 = index_3 = - 1
        for l in range(0, n + 1):
            index = 0
            vmin = (1e15)
            for r in range(l, n + 1):
                if sum [r] < vmin:
                    vmin = sum [r]
                    index = r
                if sum [l] + sum [r] - vmin > ans:
                    ans = sum [l] + sum [r] - vmin
                    index_1 = l
                    index_2 = index
                    index_3 = r
        print(str(index_1) + " " + str(index_2) + " " + str(index_3), end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [- 1, 2, 3]
        n = len(arr)
        GFG.find_Indices(arr, n)
