class GFG:
    @staticmethod
    def SubString(str, n):
        for i in range(0, n):
            for j in range(i + 1, n + 1):
                print(str[i:j])
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "abcd"
        GFG.SubString(str, len(str))
