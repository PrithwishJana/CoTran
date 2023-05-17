class GFG:
    @staticmethod
    def printMinIndexChar(str, patt):
        minIndex = Integer.MAX_VALUE
        m = len(str)
        n = len(patt)
        for i in range(0, n):
            for j in range(0, m):
                if patt[i] == str[j] and j < minIndex:
                    minIndex = j
                    break
        if minIndex != Integer.MAX_VALUE:
            print("Minimum Index Character = " + str[minIndex])
        else:
            print("No character present")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeksforgeeks"
        patt = "set"
        GFG.printMinIndexChar(str, patt)
