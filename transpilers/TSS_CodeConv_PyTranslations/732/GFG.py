class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPalindrome(s):
        i = 0
        while i < len(s):
            if s[i] != s[len(s) - i - 1]:
                return False
            i += 1
        return True
    @staticmethod
    def ans(s):
        s2 = s
        i = 0
        while i < len(s):
            s2 = s2[len(s2) - 1] + s2
            s2 = s2[0:len(s2) - 1]
            if (s2 is not None if s is None else ( s != s2)) and GFG.isPalindrome(s2):
                return True
            i += 1
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(s):
        if len(s) <= 3:
            return - 1
        cnt = [0 for _ in range(25)]
        i = 0
        while i < len(s):
            cnt [s[i] - 'a'] += 1
            i += 1
        if java.util.Arrays.stream(cnt).max().getAsInt() >= (len(s) - 1):
            return - 1
        else:
            return (1 if GFG.ans(s) else 2)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "nolon"
        print(GFG.solve(s))
