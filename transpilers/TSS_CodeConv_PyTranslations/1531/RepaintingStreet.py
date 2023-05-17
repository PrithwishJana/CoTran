class RepaintingStreet:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = sc.nextInt()
            k = sc.nextInt()
            a = [0 for _ in range(n)]
            l = []
            for i in range(0, n):
                a [i] = sc.nextInt()
                if (not a [i]) in l:
                    l.append(a [i])
            ans = Integer.MAX_VALUE
            for j, unusedItem in enumerate(l):
                moves = 0
                big = l[j]
                i = 0
                while i < n:
                    if a [i] == big:
                        i += 1
                        continue
                    moves += 1
                    i += k
                ans = min(moves, ans)
            print(ans)
        t -= 1
