class GFG:
    @staticmethod
    def findNthOccur(str, ch, N):
        occur = 0
        i = 0
        while i < len(str):
            if str[i] == ch:
                occur += 1
            if occur == N:
                return i
            i += 1
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeks"
        ch = 'e'
        N = 2
        print(GFG.findNthOccur(str, ch, N), end = '')
