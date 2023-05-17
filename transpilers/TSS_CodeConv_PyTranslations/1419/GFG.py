class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findDivisors(n):
        div = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            j = 1
            while j * i <= n:
                div [i * j] += 1
                j += 1
        for i in range(1, n + 1):
            print(str(div [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        GFG.findDivisors(n)
