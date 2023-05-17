class GFG:
    @staticmethod
    def isAlphabaticOrder(s):
        n = len(s)
        c = ['\0' for _ in range(n)]
        for i in range(0, n):
            c [i] = s[i]
        c.sort()
        for i in range(0, n):
            if c [i] != s[i]:
                return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "aabbbcc"
        if GFG.isAlphabaticOrder(s):
            print("Yes")
        else:
            print("No")
