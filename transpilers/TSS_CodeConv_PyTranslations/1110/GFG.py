class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isVowel(ch):
        if (ch == 'a') or (ch == 'e') or (ch == 'i') or (ch == 'o') or (ch == 'u'):
            return True
        return False
    @staticmethod
    def isSatisfied(str, n):
        for i in range(1, n):
            if (not GFG.isVowel(str [i])) and not GFG.isVowel(str [i - 1]):
                return False
        i = 1
        while i < n - 1:
            if GFG.isVowel(str [i]) and (not GFG.isVowel(str [i - 1])) and not GFG.isVowel(str [i + 1]):
                return False
            i += 1
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "acaba"
        n = len(str)
        if GFG.isSatisfied(str.toCharArray(), n):
            print("Yes")
        else:
            print("No")
