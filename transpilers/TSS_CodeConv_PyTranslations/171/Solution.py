import math

class Solution:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        s = sc.nextInt()
        k = 0
        count = 0
        for i in range(n, 0, -1):
            k = math.trunc(s / float(i))
            count += k
            s -= k * i
        print(count)
