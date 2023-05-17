class GFG:
    @staticmethod
    def maxSubStr(str, n):
        count0 = 0
        count1 = 0
        cnt = 0
        for i in range(0, n):
            if str[i] == '0':
                count0 += 1
            else:
                count1 += 1
            if count0 == count1:
                cnt += 1
        if count0 != count1:
            return - 1
        return cnt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "0100110101"
        n = len(str)
        print(GFG.maxSubStr(str, n))
