class GFG:
    sum = 0
    N = 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getAvg(x):
        GFG.sum += x
        n += 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: return (((float) sum) / ++ n);
        return ((float(GFG.sum)) /  GFG.N)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def streamAvg(arr, n):
        avg = 0
        for i in range(0, n):
            avg = GFG.getAvg(int(arr [i]))
            print("Average of " + str(i + 1) + " numbers is " + str(avg))
        return
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 20, 30, 40, 50, 60]
        n = len(arr)
        GFG.streamAvg(arr, n)
