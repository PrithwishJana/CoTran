class Solution10:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
        str = StringBuilder()
        for z in range(0, t):
            n = sc.nextInt()
            x = sc.nextInt()
            m = sc.nextInt()
            arr = [[0 for _ in range(2)] for _ in range(m)]
            for i in range(0, m):
                arr [i][0] = sc.nextInt()
                arr [i][1] = sc.nextInt()
            si = x
            ei = x
            for i in range(0, m):
                l = arr [i][0]
                r = arr [i][1]
                if (l <= si and si <= r) or (l <= ei and ei <= r):
                    si = min(l, si)
                    ei = max(r, ei)
            str.append(ei - si + 1)
            str.append("\n")
        print(str(str))
