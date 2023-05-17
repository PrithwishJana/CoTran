class GFG:
    @staticmethod
    def isValid(str, len):
        for i in range(1, len):
            if str[i] == str[i - 1]:
                return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "0110"
        len = len(str)
        if GFG.isValid(str, len):
            print("Valid")
        else:
            print("Invalid")
