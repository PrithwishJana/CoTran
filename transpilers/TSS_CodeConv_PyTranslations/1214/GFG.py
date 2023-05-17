class GFG:
    @staticmethod
    def MaxTotalRectangleArea(a, n):
        a.sort()
        sum = 0
        flag = False
        len = 0
        i = 0
        while i < n:
            if (a [i] == a [i + 1] or a [i] - a [i + 1] == 1) and not flag:
                flag = True
                len = a [i + 1]
                i += 1
            elif (a [i] == a [i + 1] or a [i] - a [i + 1] == 1) and (flag):
                sum = sum + a [i + 1] * len
                flag = False
                i += 1
            i += 1
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [10, 10, 10, 10, 11, 10, 11, 10, 9, 9, 8, 8]
        n = len(a)
        print(GFG.MaxTotalRectangleArea(a, n), end = '')
