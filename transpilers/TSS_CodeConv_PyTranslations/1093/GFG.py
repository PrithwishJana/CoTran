class GFG:
    @staticmethod
    def getSmallestAndLargest(s, k):
        currStr = s[0:k]
        lexMin = currStr
        lexMax = currStr
        i = k
        while i < len(s):
            currStr = currStr[1:k] + s[i]
            if lexMax < currStr:
                lexMax = currStr
            if lexMin > currStr:
                lexMin = currStr
            i += 1
        print(lexMin)
        print(lexMax)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "GeeksForGeeks"
        k = 3
        GFG.getSmallestAndLargest(str, k)
