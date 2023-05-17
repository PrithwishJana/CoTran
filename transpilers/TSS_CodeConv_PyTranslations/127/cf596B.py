class cf596B:
    @staticmethod
    def main(args):
        scan = Scanner(System.in)
        n = scan.nextInt()
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            arr [i] = scan.nextInt()
        answer = abs(arr [0])
        for i in range(1, n):
            answer += abs(arr [i] - arr [i - 1])
        print(answer)
