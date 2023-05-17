class GFG:
    @staticmethod
    def findLength(str, n):
        ans = 0
        i = 0
        while i <= n - 2:
            l = i
            r = i + 1
            lsum = 0
            rsum = 0
            while r < n and l >= 0:
                lsum += str[l] - '0'
                rsum += str[r] - '0'
                if lsum == rsum:
                    ans = max(ans, r - l + 1)
                l -= 1
                r += 1
            i += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "123123"
        print("Length of the substring is " + str(GFG.findLength(str, len(str))))
