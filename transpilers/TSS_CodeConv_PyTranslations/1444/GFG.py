class GFG:
    @staticmethod
    def intersection(a, b, n, m):
        i = 0
        j = 0
        while i < n and j < m:
            if a [i] > b [j]:
                j += 1
            elif b [j] > a [i]:
                i += 1
            else:
                print(str(a [i]) + " ", end = '')
                i += 1
                j += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 2, 3, 3, 4, 5, 5, 6]
        b = [3, 3, 5]
        n = len(a)
        m = len(b)
        GFG.intersection(a, b, n, m)
