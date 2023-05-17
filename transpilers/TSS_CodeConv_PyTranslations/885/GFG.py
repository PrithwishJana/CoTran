class GFG:
    @staticmethod
    def extractMaximum(str):
        num = 0
        res = 0
        i = 0
        while i < len(str):
            if (str[i]).isdigit():
                num = num * 10 + (str[i] - '0')
            else:
                res = max(res, num)
                num = 0
            i += 1
        return max(res, num)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "100klh564abc365bg"
        print(GFG.extractMaximum(str))
