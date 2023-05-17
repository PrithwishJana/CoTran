import math

class HelloWorld:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        scan = Scanner(System.in)
        a = scan.nextInt()
        b = scan.nextInt()
        res = a
        while a >= b:
            res += (math.trunc(a / float(b)))
            a = (math.trunc(a / float(b))) + (math.fmod(a, b))
        print(res)
