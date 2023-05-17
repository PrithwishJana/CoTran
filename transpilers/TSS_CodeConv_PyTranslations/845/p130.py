import math

class p130:
    @staticmethod
    def main(args):
        print((p130()).run())
    def run(self):
        sum = 0
        found = 0
        i = 7
        while found < 25:
            if math.fmod(i, 5) != 0 and (not Library.isPrime(i)) and math.fmod((i - 1), p130._findLeastDivisibleRepunit(i)) == 0:
                sum += i
                found += 1
            i += 2
        return str(sum)
    @staticmethod
    def _findLeastDivisibleRepunit(n):
        if math.fmod(n, 2) == 0 or math.fmod(n, 5) == 0:
            return 0
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        if n > Integer.MAX_VALUE / 10:
            raise IllegalArgumentException("Arithmetic overflow")
        sum = 1
        pow = 1
        k = 1
        while math.fmod(sum, n) != 0:
            k += 1
            pow = math.fmod(pow * 10, n)
            sum = math.fmod((sum + pow), n)
        return k
