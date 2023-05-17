class ProblemB:
    @staticmethod
    def main(args):
        scn = Scanner(System.in)
        n = scn.nextInt()
        arr = [0 for _ in range(n)]
        i = 0
        while i < len(arr):
            arr [i] = scn.nextInt()
            i += 1
        ans = arr [0] + 1
        i = 1
        while i < len(arr):
            ans += abs(arr [i] - arr [i - 1]) + 2
            i += 1
        print(ans)
