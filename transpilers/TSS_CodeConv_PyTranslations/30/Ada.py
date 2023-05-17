import math

class Ada:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        n = sc.nextInt()
        m = sc.nextInt()
        dp = [0 for _ in range(n + 1)]
        pre = [0 for _ in range(n + 1)]
        prevSum = dp [1] = 1
        for i in range(1, n + 1):
            if i != 1:
                pre [i] = math.fmod((pre [i - 1] + pre [i]), m)
                dp [i] = math.fmod((prevSum + pre [i]), m)
                prevSum = math.fmod((prevSum + dp [i]), m)
            p = 2
            j = 2 * i
            while j <= n:
                r = j + p
                pre [j] = math.fmod((pre [j] + dp [i]), m)
                if r <= n:
                    pre [r] = math.fmod((math.fmod((pre [r] - dp [i]), m) + m), m)
                p += 1
                j = p * i
        print(dp [n])
