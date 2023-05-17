class GFG:
    @staticmethod
    def countConsecutive(n):
        s = str(n)
        count = 0
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                count += 1
            i += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 44522255
        print(GFG.countConsecutive(n))
