class Solution:
    def toHex(self, num):
        hex_map = "0123456789abcdef"
        if num == 0:
            return "0"
        res = ""
        while num != 0 and len(res) < 8:
            res = hex_map[num & 15] + res
            num = num >> 4
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        n = 26
        out = sObj.toHex(n)
        print(out)
