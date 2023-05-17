import math

class GFG:
    @staticmethod
    def reverseDigits(num):
        rev_num = 0
        while num > 0:
            rev_num = rev_num * 10 + math.fmod(num, 10)
            num = math.trunc(num / float(10))
        return rev_num
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPalindrome(n):
        rev_n = GFG.reverseDigits(n)
        if rev_n == n:
            return 1
        else:
            return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4562
        print("Is " + str(n) + " a Palindrome number? -> " + ("True" if GFG.isPalindrome(n) == 1 else "False"))
        n = 2002
        print("Is " + str(n) + " a Palindrome number? -> " + ("True" if GFG.isPalindrome(n) == 1 else "False"))
