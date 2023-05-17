class TheRank:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        n = in_.nextInt()
        ans = 0
        rank = 1
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            a = in_.nextInt()
            b = in_.nextInt()
            c = in_.nextInt()
            d = in_.nextInt()
            sum = a + b + c + d
            arr [i] = sum
        for j in arr:
            if arr [0] < j:
                rank += 1
        print(rank)
