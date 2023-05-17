class Sol:
    @staticmethod
    def main(argc):
        sc = Scanner(System.in)
        l = sc.nextInt()
        r = sc.nextInt()
        ans = 0
        i = 1
        while i <= r:
            j = 1
            while j * i <= r:
                if i * j >= l:
                    ans += 1
                j *= 3
            i *= 2
        print(ans)
