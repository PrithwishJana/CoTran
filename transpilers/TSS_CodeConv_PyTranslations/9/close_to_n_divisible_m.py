import math

class close_to_n_divisible_m:
    @staticmethod
    def closestNumber(n, m):
        q = math.trunc(n / float(m))
        n1 = m * q
        n2 = (m * (q + 1)) if (n * m) > 0 else (m * (q - 1))
        if abs(n - n1) < abs(n - n2):
            return n1
        return n2
    @staticmethod
    def main(args):
        n = 13
        m = 4
        print(close_to_n_divisible_m.closestNumber(n, m))
        n = - 15
        m = 6
        print(close_to_n_divisible_m.closestNumber(n, m))
        n = 0
        m = 8
        print(close_to_n_divisible_m.closestNumber(n, m))
        n = 18
        m = - 7
        print(close_to_n_divisible_m.closestNumber(n, m))
