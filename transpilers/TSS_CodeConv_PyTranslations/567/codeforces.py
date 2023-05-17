class codeforces:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        if (n & (n - 1)) == 0:
            print("YES")
        else:
            print("NO")
