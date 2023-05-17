class GFG:
    @staticmethod
    def largestPalinSub(s):
        res = ""
        mx = s[0]
        i = 1
        while i < len(s):
            mx = chr(max(ord(mx), ord(s[i])))
            i += 1
        i = 0
        while i < len(s):
            if s[i] == mx:
                res += s[i]
            i += 1
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "geeksforgeeks"
        print(GFG.largestPalinSub(s))
