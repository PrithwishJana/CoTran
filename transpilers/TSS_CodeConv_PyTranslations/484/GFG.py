class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPalindrome(str):
        l = 0
        h = len(str) - 1
        while h > l:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: if (str.charAt(l ++) != str.charAt(h --))
            if str[l] != str[h]:
                h -= 1
                l += 1
                return False
            else:
                h -= 1
                l += 1
        return True
    @staticmethod
    def minRemovals(str):
        if str[0] == chr(0):
            return 0
        if GFG.isPalindrome(str):
            return 1
        return 2
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(GFG.minRemovals("010010"))
        print(GFG.minRemovals("0100101"))
