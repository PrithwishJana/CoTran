import math

class GFG:
    one = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
    ten = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
    @staticmethod
    def numToWords(n, s):
        str = ""
        if n > 19:
            str += GFG.ten [math.trunc(n / float(10))] + GFG.one [math.fmod(n, 10)]
        else:
            str += GFG.one [n]
        if n != 0:
            str += s
        return str
    @staticmethod
    def convertToWords(n):
        out = ""
        out += GFG.numToWords(int((math.trunc(n / float(10000000)))), "crore ")
        out += GFG.numToWords(int((math.fmod((math.trunc(n / float(100000))), 100))), "lakh ")
        out += GFG.numToWords(int((math.fmod((math.trunc(n / float(1000))), 100))), "thousand ")
        out += GFG.numToWords(int((math.fmod((math.trunc(n / float(100))), 10))), "hundred ")
        if n > 100 and math.fmod(n, 100) > 0:
            out += "and "
        out += GFG.numToWords(int((math.fmod(n, 100))), "")
        return out
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 438237764
        print(GFG.convertToWords(n))
