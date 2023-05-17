class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isVowel(ch):
        if (ch == 'a') or (ch == 'e') or (ch == 'i') or (ch == 'o') or (ch == 'u'):
            return True
        else:
            return False
    @staticmethod
    def vowelPairs(s, n):
        cnt = 0
        i = 0
        while i < n - 1:
            if GFG.isVowel(s[i]) and GFG.isVowel(s[i + 1]):
                cnt += 1
            i += 1
        return cnt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "abaebio"
        n = len(s)
        print(GFG.vowelPairs(s, n), end = '')
