class GFG:
    @staticmethod
    def flipSign(a):
        neg = 0
        tmp = 1 if a < 0 else - 1
        while a != 0:
            neg += tmp
            a += tmp
        return neg
    @staticmethod
    def areDifferentSign(a, b):
        return (or (a > 0 and b < 0))
    @staticmethod
    def sub(a, b):
        return a + GFG.flipSign(b)
    @staticmethod
    def mul(a, b):
        if a < b:
            return GFG.mul(b, a)
        sum = 0
        for i in range(abs(b), 0, -1):
            sum += a
        if b < 0:
            sum = GFG.flipSign(sum)
        return sum
    @staticmethod
    def division(a, b):
        if b == 0:
            raise ArithmeticException()
        quotient = 0
        dividend = 0
        divisor = GFG.flipSign(abs(b))
        dividend = Math.abs(a)
        while dividend >= abs(divisor):
            quotient += 1
            dividend += divisor
        if GFG.areDifferentSign(a, b):
            quotient = GFG.flipSign(quotient)
        return quotient
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print("Subtraction is " + str(GFG.sub(4, - 2)))
        print("Product is " + str(GFG.mul(- 9, 6)))
        try:
            print("Division is " + str(GFG.division(8, 2)))
        except ArithmeticException as e:
            print("Exception :- Divide by 0")
