import math

class S:
    @staticmethod
    def main(args):
        in_ = Scanner(System.in)
        n = in_.nextInt()
        cntp = [0 for _ in range(11)]
        cntn = [0 for _ in range(11)]
        cnt = 0
        for i in range(0, n):
            a = in_.nextInt()
            if a == 0:
                cnt += 1
            elif a > 0:
                cntp [a] += 1
            elif a < 0:
                cntn [abs(a)] += 1
        res = 0
        for i in range(1, 11):
            res = res + (cntp [i] * cntn [i])
        res = res + (math.trunc((cnt * (cnt - 1)) / float(2)))
        print(res, end = '')
