import math

class GFG:
    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    @staticmethod
    def printWordsWithoutIfSwitch(n):
        digits = [0 for _ in range(10)]
        dc = 0
        loop_condition = True
        while loop_condition:
            digits [dc] = math.fmod(n, 10)
            n = math.trunc(n / float(10))
            dc += 1
            loop_condition = n != 0
        for i in range(dc - 1, -1, -1):
            print(GFG.word [digits [i]] + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 350
        GFG.printWordsWithoutIfSwitch(n)
