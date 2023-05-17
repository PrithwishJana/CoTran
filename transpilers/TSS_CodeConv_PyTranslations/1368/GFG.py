class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findNumber(N, S):
        i = ((float((N)) * float((N + 1))) / 4) - (float((S + 1)) / 2)
        return i
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(N, S):
        i = GFG.findNumber(N, S)
        integerI = int(i)
        if i - integerI == 0:
            print("Yes: " + str(integerI) + ", " + str(integerI + 1))
        else:
            print("No")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 4
        S = 3
        GFG.check(N, S)
        N = 5
        S = 3
        GFG.check(N, S)
