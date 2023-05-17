class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isVowel(c):
        return (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def encryptString(s, n, k):
        countVowels = 0
        countConsonants = 0
        ans = ""
        l = 0
        while l <= n - k:
            countVowels = 0
            countConsonants = 0
            r = l
            while r <= l + k - 1:
                if GFG.isVowel(s[r]) == True:
                    countVowels += 1
                else:
                    countConsonants += 1
                r += 1
            ans += str(countVowels * countConsonants)
            l += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "hello"
        n = len(s)
        k = 2
        print(GFG.encryptString(s, n, k))
