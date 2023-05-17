import math

class GFG:
    @staticmethod
    def evenNumSubstring(str):
        len = len(str)
        count = 0
        for i in range(0, len):
            temp = str[i] - '0'
            if math.fmod(temp, 2) == 0:
                count += (i + 1)
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "1234"
        print(GFG.evenNumSubstring(str))
