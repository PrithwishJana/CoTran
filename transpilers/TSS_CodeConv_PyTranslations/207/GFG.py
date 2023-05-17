import math

class GFG:
    @staticmethod
    def nthPalindrome(n, k):
        temp = (math.trunc(k / float(2))) if (k & 1) != 0 else (math.trunc(k / float(2)) - 1)
        palindrome = int(10) ** temp
        palindrome += n - 1
        print(palindrome, end = '')
        if (k & 1) > 0:
            palindrome = math.trunc(palindrome / float(10))
        while palindrome > 0:
            print(math.fmod(palindrome, 10), end = '')
            palindrome = math.trunc(palindrome / float(10))
        print("")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        k = 5
        print(str(n) + "th palindrome of " + str(k) + " digit = ", end = '')
        GFG.nthPalindrome(n, k)
        n = 10
        k = 6
        print(str(n) + "th palindrome of " + str(k) + " digit = ", end = '')
        GFG.nthPalindrome(n, k)
