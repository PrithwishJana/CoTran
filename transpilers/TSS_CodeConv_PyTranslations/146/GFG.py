class GFG:
    @staticmethod
    def startsWith(str, pre):
        strLen = len(str)
        preLen = len(pre)
        i = 0
        j = 0
        while i < strLen and j < preLen:
            if str[i] != pre[j]:
                return False
            i += 1
            j += 1
        return True
    @staticmethod
    def endsWith(str, suff):
        i = len(str) - 1
        j = len(suff) - 1
        while i >= 0 and j >= 0:
            if str[i] != suff[j]:
                return False
            i -= 1
            j -= 1
        return True
    @staticmethod
    def checkString(str, a, b):
        if len(str) != len(a) + len(b):
            return False
        if GFG.startsWith(str, a):
            if GFG.endsWith(str, b):
                return True
        if GFG.startsWith(str, b):
            if GFG.endsWith(str, a):
                return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "GeeksforGeeks"
        a = "Geeksfo"
        b = "rGeeks"
        if GFG.checkString(str, a, b):
            print("Yes")
        else:
            print("No")
