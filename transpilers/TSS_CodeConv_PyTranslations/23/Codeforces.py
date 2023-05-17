class Codeforces:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            arr [i] = sc.nextInt()
            arr [i] = arr [i] - 1
        lt = False
        for i in range(0, n):
            if i == arr [arr [arr [i]]]:
                lt = True
                break
        if lt:
            print("YES")
        else:
            print("NO")
