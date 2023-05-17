class GFG:
    st = HashSet()
    @staticmethod
    def generateNumbers(n, num, a, b):
        if num > 0 and num < n:
            GFG.st.add(num)
        if num >= n:
            return
        if num * 10 + a > num:
            GFG.generateNumbers(n, num * 10 + a, a, b)
        GFG.generateNumbers(n, num * 10 + b, a, b)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printNumbers(n):
        for i in range(0, 10):
            for j in range(i + 1, 10):
                GFG.generateNumbers(n, 0, i, j)
        print("The numbers are: ", end = '')
        print(GFG.st, end = '')
        GFG.st.clear()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 12
        GFG.printNumbers(n)
