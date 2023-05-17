import math

class GFG:
    @staticmethod
    def possibleTripletInRange(L, R):
        flag = False
        possibleA = 0
        possibleB = 0
        possibleC = 0
        numbersInRange = (R - L + 1)
        if numbersInRange < 3:
            flag = False
        elif numbersInRange > 3:
            flag = True
            if math.fmod(L, 2) > 0:
                L += 1
            possibleA = L
            possibleB = L + 1
            possibleC = L + 2
        else:
            if not(math.fmod(L, 2) > 0):
                flag = True
                possibleA = L
                possibleB = L + 1
                possibleC = L + 2
            else:
                flag = False
        if flag == True:
            print("(" + str(possibleA) + ", " + str(possibleB) + ", " + str(possibleC) + ")" + " is one such possible" + " triplet between " + str(L) + " and " + str(R))
        else:
            print("No Such Triplet" + " exists between " + str(L) + " and " + str(R))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        L = 0
        R = 0
        L = 2
        R = 10
        GFG.possibleTripletInRange(L, R)
        L = 23
        R = 46
        GFG.possibleTripletInRange(L, R)
