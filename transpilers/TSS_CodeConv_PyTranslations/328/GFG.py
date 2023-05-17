class GFG:
    PHI = 1.6180339
    f = [0, 1, 1, 2, 3, 5]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def fib(n):
        if n < 6:
            return GFG.f [n]
        t = 5
        fn = 5
        while t < n:
            fn = int(round(fn * GFG.PHI))
            t += 1
        return fn
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 9
        print(str(n) + "th Fibonacci Number = " + str(GFG.fib(n)))
