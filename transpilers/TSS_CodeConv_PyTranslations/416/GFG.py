class GFG:
    @staticmethod
    def isSmaller(str1, str2):
        n1 = len(str1)
        n2 = len(str2)
        if n1 < n2:
            return True
        if n2 < n1:
            return False
        for i in range(0, n1):
            if str1[i] < str2[i]:
                return True
            elif str1[i] > str2[i]:
                return False
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findDiff(str1, str2):
        if GFG.isSmaller(str1, str2):
            t = str1
            str1 = str2
            str2 = t
        str = ""
        n1 = len(str1)
        n2 = len(str2)
        str1 = str((StringBuilder(str1)).reverse())
        str2 = str((StringBuilder(str2)).reverse())
        carry = 0
        for i in range(0, n2):
            sub = (int((str1[i] - '0')) - int((str2[i] - '0')) - carry)
            if sub < 0:
                sub = sub + 10
                carry = 1
            else:
                carry = 0
            str += chr((sub + '0'))
        for i in range(n2, n1):
            sub = (int((str1[i] - '0')) - carry)
            if sub < 0:
                sub = sub + 10
                carry = 1
            else:
                carry = 0
            str += chr((sub + '0'))
        return str((StringBuilder(str)).reverse())
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str1 = "978"
        str2 = "12977"
        print(GFG.findDiff(str1, str2))
        s1 = "100"
        s2 = "1000000"
        print(GFG.findDiff(s1, s2))
