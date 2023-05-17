import math

class Test:
    @staticmethod
    def factorial(n):
        i = n
        fact = 1
        while math.trunc(n / float(i)) != n:
            fact = fact * i
            i -= 1
        return fact
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        num = 5
        print("Factorial of " + str(num) + " is " + str(Test.factorial(5)))
