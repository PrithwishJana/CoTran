import math

class Solution:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        s = sc.next()
        count = 0
        for i in range(0, n):
            if s[i] == '8':
                count += 1
        print(min(count, math.trunc(n / float(11))))
