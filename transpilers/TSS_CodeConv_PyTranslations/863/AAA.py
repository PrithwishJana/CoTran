import math

class AAA:
    @staticmethod
    def get_last_two_digit(N):
        if N <= 10:
            ans = 0
            fac = 1
            for i in range(1, N + 1):
                fac = fac * i
                ans += fac
            return math.fmod(int(ans), 100)
        else:
            return 13
    @staticmethod
    def main(args):
        N = 1
        for N in range(1, 11):
            print("For N = " + str(N) + " : " + str(AAA.get_last_two_digit(N)))
