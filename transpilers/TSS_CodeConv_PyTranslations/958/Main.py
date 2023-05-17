import math

class Solution:
    def longestPalindrome(self, s):
        count = [0 for _ in range(128)]
        for c in s.toCharArray():
            count [c] += 1
        ans = 0
        for v in count:
            ans += math.trunc(v / float(2 * 2))
            if math.fmod(ans, 2) == 0 and math.fmod(v, 2) == 1:
                ans += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        s = "abccccdd"
        out = sObj.longestPalindrome(s)
        print(out)
