class GFG:
    @staticmethod
    def findS(s):
        sum = 0
        n = 1
        while sum < s:
            sum += n
            if sum == s:
                return n
            n += 1
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = 15
        n = GFG.findS(s)
        if n == - 1:
            print("-1")
        else:
            print(n)
