class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getAvg(prev_avg, x, n):
        return (prev_avg * n + x) / (n + 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def streamAvg(arr, n):
        avg = 0
        for i in range(0, n):
            avg = GFG.getAvg(avg, arr [i], i)
            print("Average of " + str(i + 1) + " numbers is " + "{0:.1f}".format(avg))
        return
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 20, 30, 40, 50, 60]
        n = len(arr)
        GFG.streamAvg(arr, n)
