class A:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.in_ = None

    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        (A())._solve()
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def _solve(self):
        self.in_ = Scanner(System.in)
        t = self.in_.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = self.in_.nextInt()
            message = [self.in_.next().split("")]
            self._identifyMessage(message, n)
        t -= 1
    def _identifyMessage(self, list, n):
        list.reverse()
        leftSymbols = 0
        for character in list:
            if character == ")":
                leftSymbols += 1
            else:
                break
        print("Yes" if leftSymbols > (n - leftSymbols) else "No")
