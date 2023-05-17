class practice:
    @staticmethod
    def main(args):
        scn = Scanner(System.in)
        s = scn.next()
        p = None
        k = scn.nextInt()
        x = 0
        y = 0
        ans = 0
        a = '\0'
        b = '\0'
        for i in range(0, k):
            p = scn.next()
            j = 0
            while j < len(s):
                if s[j] == p[0]:
                    x += 1
                elif s[j] == p[1]:
                    y += 1
                else:
                    ans += min(x, y)
                    x = 0
                    y = 0
                j += 1
            ans += min(x, y)
            x = 0
            y = 0
        print(ans)
