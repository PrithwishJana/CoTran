class zer:
    in_ = Scanner(System.in)
    @staticmethod
    def main(args):
        n = zer.in_.nextInt()
        m = zer.in_.nextInt()
        p = [0 for _ in range(n)]
        tab = []
        for i in range(0, n):
            p [i] = zer.in_.nextInt()
            tab.append(HashSet())
        ans = 3000003
        for i in range(0, m):
            a = zer.in_.nextInt() - 1
            b = zer.in_.nextInt() - 1
            for x in tab[a]:
                if tab[b].contains(x):
                    ans = min(p [a] + p [b] + p [x], ans)
            tab[a].add(b)
            tab[b].add(a)
        if ans == 3000003:
            print(- 1)
        else:
            print(ans)
