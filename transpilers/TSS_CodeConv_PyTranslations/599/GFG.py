class GFG:
    MAX_CHAR = chr(256)
    @staticmethod
    def maximumChars(str):
        n = len(str)
        res = - 1
        firstInd = [0 for _ in range(GFG.MAX_CHAR)]
        i = 0
        while chr(i) < GFG.MAX_CHAR:
            firstInd [i] = - 1
            i += 1
        for i in range(0, n):
            first_ind = firstInd [str[i]]
            if first_ind == - 1:
                firstInd [str[i]] = i
            else:
                res = max(res, abs(i - first_ind - 1))
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "abba"
        print(GFG.maximumChars(str))
