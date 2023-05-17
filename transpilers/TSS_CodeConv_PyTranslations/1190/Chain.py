class Chain:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        max = 0
        n = sc.nextInt()
        beacon = [0 for _ in range(1000001)]
        dp = [0 for _ in range(1000001)]
        for i in range(0, n):
            a = sc.nextInt()
            beacon [a] = sc.nextInt()
        if beacon [0] != 0:
            dp [0] = 1
        for i in range(1, 1000001):
            if beacon [i] != 0 and beacon [i] < i:
                dp [i] = dp [i - beacon [i] - 1] + 1
            elif beacon [i] != 0:
                dp [i] = 1
            else:
                dp [i] = dp [i - 1]
            max = max(max, dp [i])
        print(n - max, end = '')
