class GFG:
    @staticmethod
    def knapSack(W, wt, val, n):
        maxratio = Integer.MIN_VALUE
        maxindex = 0
        for i in range(0, n):
            if (val [i] / wt [i]) > maxratio:
                maxratio = (val [i] / wt [i])
                maxindex = i
        return (W * maxratio)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        val = [14, 27, 44, 19]
        wt = [6, 7, 9, 8]
        n = len(val)
        W = 50
        print(GFG.knapSack(W, wt, val, n))
