import math

class A:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.in_ = None

    @staticmethod
    def power(a):
        res = 0
        while a > 0:
            res += 1
            a = math.trunc(a / float(10))
        return res
    @staticmethod
    def mult(a):
        pow = A.power(a)
        max = 0
        for j in range(0, pow):
            max = max * 10 + 9
        return a * (max - a)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = java.util.Scanner(System.in)
        l = in_.nextLong()
        r = in_.nextLong()
        res = 0
        maxxes = [0 for _ in range(10)]
        temp = 0
        for i in range(0, 10):
            temp = temp * 10 + 9
            maxxes [i] = math.trunc(temp / float(2 * (temp - math.trunc(temp / float(2)))))
        res = max(A.mult(l), res)
        res = max(A.mult(r), res)
        temp = 0
        for i in range(0, 10):
            temp = temp * 10 + 9
            if l <= math.trunc(temp / float(2)) and math.trunc(temp / float(2)) <= r:
                res = max(maxxes [i], res)
        print(res)
