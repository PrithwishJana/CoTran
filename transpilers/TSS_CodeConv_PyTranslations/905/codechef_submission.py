class codechef_submission:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        n = sc.nextInt()
        m = sc.nextInt()
        k = sc.nextInt()
        b = [0 for _ in range(n)]
        if n < k:
            print(n)
            return
        for i in range(0, n):
            b [i] = sc.nextInt()
        d = [0 for _ in range(n - 1)]
        i = 0
        while i < n - 1:
            d [i] = b [i + 1] - b [i] - 1
            i += 1
        d.sort()
        sum = b [len(b) - 1] - b [0] + 1
        i = d.length - 1
        while i > len(d) - 1 - (k - 1):
            sum -= d [i]
            i -= 1
        print(sum)
