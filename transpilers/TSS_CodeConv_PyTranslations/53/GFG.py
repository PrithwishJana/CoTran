import math

class GFG:
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def fib(self, f):
        f [0] = 0
        f [1] = 1
        for i in range(2, 60):
            f [i] = math.fmod((f [i - 1] + f [i - 2]), 10)
    def findLastDigit(self, n):
        f = [0 for _ in range(60)]
        self.fib(f)
        index = int((math.fmod(n, 60)))
        return f [index]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 0
        ob = GFG()
        n = 1
        print(ob.findLastDigit(n))
        n = 61
        print(ob.findLastDigit(n))
        n = 7
        print(ob.findLastDigit(n))
        n = 67
        print(ob.findLastDigit(n))
