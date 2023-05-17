class Solution:
    def isPerfectSquare(self, num):
        low = 1
        high = num
        while low <= high:
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java's unsigned right shift operator:
            mid = (low + high) >>> 1
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = int(mid) + 1
            else:
                high = int(mid) - 1
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        n = 16
        out = sObj.isPerfectSquare(n)
        print(out)
