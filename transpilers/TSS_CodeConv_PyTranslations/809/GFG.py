class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxSum(a, n):
        l = list  ()
        s = 0
        for i in range(0, n):
            s += abs(a [i])
            if a [i] >= 0:
                continue
            if i == 0:
                l.append(i + 1)
            else:
                l.append(i + 1)
                l.append(i)
        print(s)
        for i, unusedItem in enumerate(l):
            print(str(l[i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        a = [1, - 2, - 3, 4]
        GFG.maxSum(a, n)
