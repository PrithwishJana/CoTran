class GFG:
    @staticmethod
    def countOfLetters(str):
        letter = 0
        i = 0
        while i < len(str):
            if (str[i] >= 'A' and str[i] <= 'Z') or (str[i] >= 'a' and str[i] <= 'z'):
                letter += 1
            i += 1
        return letter
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countOfNumbers(str):
        number = 0
        i = 0
        while i < len(str):
            if str[i] >= '0' and str[i] <= '9':
                number += 1
            i += 1
        return number
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(str):
        if GFG.countOfLetters(str) == GFG.countOfNumbers(str):
            print("Yes\n", end = '')
        else:
            print("No\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "GeeKs01324"
        GFG.check(str)
