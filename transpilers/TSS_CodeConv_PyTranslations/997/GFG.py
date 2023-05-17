class GFG:
    alphabets = "abcdefghijklmnopqrstuvwxyz" .toCharArray()
    @staticmethod
    def conversion(charSet, str1):
        s2 = ""
        for i in str1:
            s2 += GFG.alphabets [charSet.find(i)]
        return s2
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        charSet = "qwertyuiopasdfghjklzxcvbnm"
        str1 = "egrt"
        print(GFG.conversion(charSet, str1.toCharArray()), end = '')
