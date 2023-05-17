import math

class GFG:
    MAX_DIGITS = 20
    @staticmethod
    def isOctal(n):
        while n > 0:
            if (math.fmod(n, 10)) >= 8:
                return 0
            else:
                n = math.trunc(n / float(10))
        return 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPalindrome(n):
        divide = 8 if (GFG.isOctal(n) == 0) else 10
        octal = [0 for _ in range(GFG.MAX_DIGITS)]
        i = 0
        while n != 0:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: octal [i ++] = n % divide;
            octal [i ] = math.fmod(n, divide)
            i += 1
            n = math.trunc(n / float(divide))
        j = i - 1
        k = 0
        while k <= j:
            if octal [j] != octal [k]:
                return 0
            j -= 1
            k += 1
        return 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 97
        if GFG.isPalindrome(n) > 0:
            print("Yes", end = '')
        else:
            print("No", end = '')
