class GFG:
    @staticmethod
    def maxSubStrings(s, k):
        maxSubStr = 0
        n = len(s)
        for c in range(0, 26):
            ch = chr((ord('a') + c))
            curr = 0
            i = 0
            while i <= n - k:
                if s[i] != ch:
                    i += 1
                    continue
                cnt = 0
                while i < n and s[i] == ch and cnt != k:
                    i += 1
                    cnt += 1
                i -= 1
                if cnt == k:
                    curr += 1
                i += 1
            maxSubStr = max(maxSubStr, curr)
        return maxSubStr
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "aaacaabbaa"
        k = 2
        print(GFG.maxSubStrings(s, k))
