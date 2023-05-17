class GFG:
    @staticmethod
    def findExtraCharcter(strA, strB):
        m1 = [0 for _ in range(256)]
        i = 0
        while i < len(strB):
            m1 [strB [i]] += 1
            i += 1
        i = 0
        while i < len(strA):
            m1 [strA [i]] -= 1
            i += 1
        i = 0
        while i < len(m1):
            if m1 [i] == 1:
                return chr(i)
            i += 1
        return Character.MIN_VALUE
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        strA = "abcd"
        strB = "cbdad"
        print(GFG.findExtraCharcter(strA.toCharArray(), strB.toCharArray()))
