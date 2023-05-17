import math

class GFG:
    @staticmethod
    def convert12(str):
        h1 = ord(str[0]) - '0'
        h2 = ord(str[1]) - '0'
        hh = h1 * 10 + h2
        Meridien = None
        if hh < 12:
            Meridien = "AM"
        else:
            Meridien = "PM"
        hh = math.fmod(hh, 12)
        if hh == 0:
            print("12", end = '')
            for i in range(2, 8):
                print(str[i], end = '')
        else:
            print(hh, end = '')
            for i in range(2, 8):
                print(str[i], end = '')
        print(" " + Meridien)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(ar):
        str = "17:35:20"
        GFG.convert12(str)
