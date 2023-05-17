class Solution:
    def firstUniqChar(self, s):
        freq = [0 for _ in range(26)]
        i = 0
        while i < len(s):
            freq [s[i] - 'a'] += 1
            i += 1
        i = 0
        while i < len(s):
            if freq [s[i] - 'a'] == 1:
                return i
            i += 1
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        s = "leetcode"
        out = sObj.firstUniqChar(s)
        print(out)
