class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isVowel(c):
        return (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def encryptString(s, n, k):
        cv = [0 for _ in range(n)]
        cc = [0 for _ in range(n)]
        if GFG.isVowel(s [0]):
            cv [0] = 1
        else:
            cc [0] = 1
        for i in range(1, n):
            cv [i] = cv [i - 1] + (1 if GFG.isVowel(s [i]) == True else 0)
            cc [i] = cc [i - 1] + (0 if GFG.isVowel(s [i]) == True else 1)
        ans = ""
        prod = 0
        prod = cc [k - 1] * cv [k - 1]
        ans += str(prod)
        i = k
        while i < len(s):
            prod = (cc [i] - cc [i - k]) * (cv [i] - cv [i - k])
            ans += str(prod)
            i += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "hello"
        n = len(s)
        k = 2
        print(GFG.encryptString(s.toCharArray(), n, k) + "\n", end = '')
