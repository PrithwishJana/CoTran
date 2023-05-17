import math

class Solution:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if b == 0:
            return a
        return Solution.__gcd(b, math.fmod(a, b))
    @staticmethod
    def findTwoNumbers(sum, gcd):
        if Solution.__gcd(gcd, sum - gcd) == gcd and sum != gcd:
            print("a = " + min(gcd, sum - gcd) + ", b = " + str(int((sum - min(gcd, sum - gcd)))))
        else:
            print(- 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sum = 8
        gcd = 2
        Solution.findTwoNumbers(sum, gcd)
