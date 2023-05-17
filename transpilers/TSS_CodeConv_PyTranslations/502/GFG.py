import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printNumbers(a, n):
        mpp = {}
        for i in range(0, n):
            num = a [i]
            j = 1
            while j * j <= num:
                if math.fmod(num, j) == 0:
                    if j != 1:
                        if j in mpp.keys():
                            mpp[j] = mpp[j] + 1
                        else:
                            mpp[j] = 1
                    if (math.trunc(num / float(j))) != j:
                        if math.trunc(num / float(j)) in mpp.keys():
                            mpp[math.trunc(num / float(j))] = mpp[math.trunc(num / float(j))] + 1
                        else:
                            mpp[math.trunc(num / float(j))] = 1
                j += 1
        maxi = 0
        for it in mpp.entrySet():
            maxi = max(it.getValue(), maxi)
        for it in mpp.entrySet():
            if it.getValue() == maxi:
                print(it.getKey() + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [12, 15, 27, 20, 40]
        n = len(a)
        GFG.printNumbers(a, n)
