class Rough_02:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            arr [i] = sc.nextLong()
        count = 1
        i = 0
        while i < n - 1:
            if arr [i] != arr [i + 1]:
                count += 1
            i += 1
        print(count)
