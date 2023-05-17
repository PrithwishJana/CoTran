class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def smallest(s):
        l = len(s)
        ans = ""
        i = 0
        while i < l - 1:
            if s[i] > s[i + 1]:
                for j in range(0, l):
                    if i != j:
                        ans += s[j]
                return ans
            i += 1
        ans = s[0:l - 1]
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "abcda"
        print(GFG.smallest(s))
