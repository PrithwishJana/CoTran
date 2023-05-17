import math

class GFG:
    @staticmethod
    def larrgestPalindrome(n):
        upper_limit = 0
        for i in range(1, n + 1):
            upper_limit *= 10
            upper_limit += 9
        lower_limit = 1 + math.trunc(upper_limit / float(10))
        max_product = 0
        for i in range(upper_limit, lower_limit - 1, -1):
            for j in range(i, lower_limit - 1, -1):
                product = i * j
                if product < max_product:
                    break
                number = product
                reverse = 0
                while number != 0:
                    reverse = reverse * 10 + math.fmod(number, 10)
                    number = math.trunc(number / float(10))
                if product == reverse and product > max_product:
                    max_product = product
        return max_product
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 2
        print(GFG.larrgestPalindrome(n), end = '')
