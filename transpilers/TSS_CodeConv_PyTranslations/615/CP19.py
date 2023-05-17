class CP19:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        t = sc.nextInt()
        k = 0
        pos = 1
        sc.nextLine()
        arr = [0 for _ in range(n)]
        i = 0
        while i < n - 1:
            arr [i] = sc.nextInt()
            i += 1
        while pos < t:
            k = pos + arr [pos - 1]
            pos = k
        if pos == t:
            print("YES")
        else:
            print("NO")
