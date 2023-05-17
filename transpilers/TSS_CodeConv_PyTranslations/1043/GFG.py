import math

class GFG:
    @staticmethod
    def checkUtil(num, dig, base):
        if dig == 1 and num < base:
            return True
        if dig > 1 and num >= base:
            dig -= 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: return checkUtil(num / base, -- dig, base);
            return GFG.checkUtil(math.trunc(num / float(base)),  dig, base)
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(num, dig):
        for base in range(2, 33):
            if GFG.checkUtil(num, dig, base):
                return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        num = 8
        dig = 3
        if GFG.check(num, dig):
            print("Yes", end = '')
        else:
            print("No", end = '')
