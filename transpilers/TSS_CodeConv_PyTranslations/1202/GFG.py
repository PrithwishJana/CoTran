import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isDivisible(S):
        n = len(S)
        if S[n - 1] != '5' and S[n - 1] != '0':
            return False
        sum = 0
        i = 0
        while i < len(S):
            sum += ord(S[i])
            i += 1
        if math.fmod(sum, 3) == 0:
            return True
        else:
            return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        S = "15645746327462384723984023940239"
        if GFG.isDivisible(S) == True:
            print("Yes")
        else:
            print("No")
        S1 = "15645746327462384723984023940235"
        if GFG.isDivisible(S1) == True:
            print("Yes")
        else:
            print("No")
