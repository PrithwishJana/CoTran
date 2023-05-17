import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printChar(str, n):
        freq = [0 for _ in range(26)]
        for i in range(0, n):
            freq [str[i] - 'a'] += 1
        for i in range(0, n):
            if math.fmod(freq [str[i] - 'a'], 2) == 1:
                print(str[i], end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeksforgeeks"
        n = len(str)
        GFG.printChar(str, n)
