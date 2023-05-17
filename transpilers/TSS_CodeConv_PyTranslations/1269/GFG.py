class GFG:
    MAX_CHAR = chr(26)
    @staticmethod
    def findAndPrintUncommonChars(str1, str2):
        present = [0 for _ in range(GFG.MAX_CHAR)]
        i = 0
        while chr(i) < GFG.MAX_CHAR:
            present [i] = 0
            i += 1
        l1 = len(str1)
        l2 = len(str2)
        for i in range(0, l1):
            present [str1[i] - 'a'] = 1
        for i in range(0, l2):
            if present [str2[i] - 'a'] == 1 or present [str2[i] - 'a'] == - 1:
                present [str2[i] - 'a'] = - 1
            else:
                present [str2[i] - 'a'] = 2
        i = 0
        while chr(i) < GFG.MAX_CHAR:
            if present [i] == 1 or present [i] == 2:
                print(chr((i + 'a')) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str1 = "characters"
        str2 = "alphabets"
        GFG.findAndPrintUncommonChars(str1, str2)
