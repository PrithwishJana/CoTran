class GFG:
    MAX_CHAR = chr(26)
    @staticmethod
    def removeChars(str, k):
        hash = [0 for _ in range(GFG.MAX_CHAR)]
        n = len(str)
        for i in range(0, n):
            hash [str[i] - 'a'] += 1
        res = ""
        for i in range(0, n):
            if hash [str[i] - 'a'] >= k:
                res += str[i]
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeksforgeeks"
        k = 2
        print(GFG.removeChars(str, k))
