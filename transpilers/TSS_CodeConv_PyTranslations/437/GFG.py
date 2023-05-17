class GFG:
    @staticmethod
    def findSubSequence(s, num):
        res = 0
        i = 0
        while num > 0:
            if (num & 1) == 1:
                res += s[i] - '0'
            i += 1
            num = num >> 1
        return res
    @staticmethod
    def combinedSum(s):
        n = len(s)
        c_sum = 0
        range = (1 << n) - 1
        for i in range(0, range + 1):
            c_sum += GFG.findSubSequence(s, i)
        return c_sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "123"
        print(GFG.combinedSum(s))
