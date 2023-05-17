class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findAnswer(str1, str2, n):
        l = 0
        r = 0
        ans = 2
        for i in range(0, n):
            if str1[i] != str2[i]:
                l = i
                break
        for i in range(n - 1, -1, -1):
            if str1[i] != str2[i]:
                r = i
                break
        if r < l:
            return 26 * (n + 1)
        elif l == r:
            return ans
        else:
            for i in range(l + 1, r + 1):
                if str1[i] != str2[i - 1]:
                    ans -= 1
                    break
            for i in range(l + 1, r + 1):
                if str1[i - 1] != str2[i]:
                    ans -= 1
                    break
            return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str1 = "toy"
        str2 = "try"
        n = len(str1)
        print(GFG.findAnswer(str1, str2, n))
