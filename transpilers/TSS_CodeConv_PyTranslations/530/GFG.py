import math

class GFG:
    @staticmethod
    def operations(op, n, k):
        i = 0
        count = 0
        nVal = 0
        min = Integer.MAX_VALUE
        for i in range(0, n):
            nVal += op [i]
            min = min(min, nVal)
            if (k + nVal) <= 0:
                return (i + 1)
        if nVal >= 0:
            return - 1
        times = math.trunc((k - abs(min)) / float(abs(nVal)))
        k = (k - (times * abs(nVal)))
        count = (times * n)
        while k > 0:
            for i in range(0, n):
                k = k + op [i]
                count += 1
                if k <= 0:
                    break
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        op = [- 60, 65, - 1, 14, - 25]
        n = len(op)
        k = 100000
        print(GFG.operations(op, n, k), end = '')
