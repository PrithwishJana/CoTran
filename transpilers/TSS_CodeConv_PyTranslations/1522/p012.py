import math

class p012:
    @staticmethod
    def main(args):
        print((p012()).run())
    def run(self):
        triangle = 0
        i = 1
        while True:
            if Integer.MAX_VALUE - triangle < i:
                raise ArithmeticException("Overflow")
            triangle += i
            if p012._countDivisors(triangle) > 500:
                return str(triangle)
            i += 1
    @staticmethod
    def _countDivisors(n):
        count = 0
        end = Library.sqrt(n)
        for i in range(1, end):
            if math.fmod(n, i) == 0:
                count += 2
        if end * end == n:
            count += 1
        return count
