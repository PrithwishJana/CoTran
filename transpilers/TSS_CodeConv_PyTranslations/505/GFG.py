class GFG:
    @staticmethod
    def checkIfStartsWithCapital(str):
        if str[0] >= 'A' and str[0] <= 'Z':
            return 1
        else:
            return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(str):
        if GFG.checkIfStartsWithCapital(str) == 1:
            print("Accepted")
        else:
            print("Not Accepted")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "GeeksforGeeks"
        GFG.check(str)
        str = "geeksforgeeks"
        GFG.check(str)
