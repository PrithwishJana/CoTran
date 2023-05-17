import math

class GFG:
    @staticmethod
    def equivalentBase4(bin):
        if bin == "00":
            return 0
        if bin == "01":
            return 1
        if bin == "10":
            return 2
        return 3
    @staticmethod
    def isDivisibleBy5(bin):
        l = len(bin)
        if math.fmod(l, 2) != 0:
            bin = '0' + bin
        odd_sum = 0
        even_sum = 0
        isOddDigit = 1
        i = 0
        while i < len(bin):
            if isOddDigit != 0:
                odd_sum += GFG.equivalentBase4(bin[i:i + 2])
            else:
                even_sum += GFG.equivalentBase4(bin[i:i + 2])
            isOddDigit ^= 1
            i += 2
        if math.fmod(abs(odd_sum - even_sum), 5) == 0:
            return "Yes"
        return "No"
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        bin = "10000101001"
        print(GFG.isDivisibleBy5(bin))
