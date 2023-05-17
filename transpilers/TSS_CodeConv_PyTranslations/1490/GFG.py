import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPalindrome(str):
        len = len(str)
        i = 0
        while i < math.trunc(len / float(2)):
            if str[i] != str[len - 1 - i]:
                return False
            i += 1
        return True
    @staticmethod
    def createStringAndCheckPalindrome(N):
        sub = "" + str(N)
        res_str = ""
        sum = 0
        while N > 0:
            digit = math.fmod(N, 10)
            sum += digit
            N = math.trunc(N / float(10))
        while len(res_str) < sum:
            res_str += sub
        if len(res_str) > sum:
            res_str = res_str[0:sum]
        if GFG.isPalindrome(res_str):
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 10101
        if GFG.createStringAndCheckPalindrome(N):
            print("Yes")
        else:
            print("No")
