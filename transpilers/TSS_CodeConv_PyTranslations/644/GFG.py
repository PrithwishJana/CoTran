class GFG:
    @staticmethod
    def longestSubstring(s):
        cnt = 1
        maxi = 1
        n = len(s)
        for i in range(1, n):
            if s[i] != s[i - 1]:
                cnt += 1
            else:
                maxi = max(cnt, maxi)
                cnt = 1
        maxi = max(cnt, maxi)
        return maxi
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "ccccdeededff"
        print(GFG.longestSubstring(s))
