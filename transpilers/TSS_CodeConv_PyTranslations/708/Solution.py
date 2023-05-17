import math

class Solution:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = Scanner(System.in)
        for t in range(in_.nextInt(), 0, -1):
            a = in_.nextInt()
            b = in_.nextInt()
            res = min(math.trunc((a + b) / float(4)), min(a, b))
            print(res)
