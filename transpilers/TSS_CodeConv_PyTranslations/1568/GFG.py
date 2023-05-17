class GFG:
    MAX = 26
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxLength(str, len):
        res = 0
        lastPos = [0 for _ in range(GFG.MAX)]
        i = 0
        while i < GFG.MAX:
            lastPos [i] = - 1
            i += 1
        for i in range(0, len):
            C = str[i] - 'a'
            if lastPos [C] != - 1:
                res = max(len - (i - lastPos [C] - 1) - 1, res)
            lastPos [C] = i
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeksforgeeks"
        len = len(str)
        print(GFG.maxLength(str, len))
