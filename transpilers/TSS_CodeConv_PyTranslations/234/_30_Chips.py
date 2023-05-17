import math

class _30_Chips:
    @staticmethod
    def main(args):
        scn = java.util.Scanner(System.in)
        n = scn.nextInt()
        k = scn.nextInt()
        row = [False for _ in range(n)]
        col = [False for _ in range(n)]
        for i in range(0, k):
            val = scn.nextInt()
            val2 = scn.nextInt()
            row [val - 1] = True
            col [val2 - 1] = True
        ans = 0
        i = 1
        while i < n - 1:
            if math.fmod(n, 2) == 1 and i == math.trunc(n / float(2)):
                if (not row [i]) or not col [i]:
                    ans += 1
            elif (not row [i]) or not col [i]:
                ans = ans + (2 if ((not row [i]) and (not col [i])) else 1)
            i += 1
        print(ans)
