class GFG:
    @staticmethod
    def checkPalindrome(str):
        len = len(str)
        len -= 1
        i = 0
        while i < len:
            if str[i] != str[len]:
                return False
            len -= 1
            i += 1
        return True
    @staticmethod
    def printSolution(partitions):
        for i in partitions:
            for j in i:
                print(j + " ", end = '')
            print()
    @staticmethod
    def addStrings(v, s, temp, index):
        len = len(s)
        str = ""
        current = list(temp)
        if index == 0:
            temp.clear()
        for i in range(index, len):
            str = str + s[i]
            if GFG.checkPalindrome(str):
                temp.append(str)
                if i + 1 < len:
                    v = GFG.addStrings(v, s, temp, i + 1)
                else:
                    v.append(temp)
                temp = list(current)
        return v
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def partition(s, v):
        temp = []
        v = GFG.addStrings(v, s, temp, 0)
        GFG.printSolution(v)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "geeks"
        partitions = []
        GFG.partition(s, partitions)
