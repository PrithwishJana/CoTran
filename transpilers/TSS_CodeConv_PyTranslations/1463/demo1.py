import math

class demo1:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            arr [i] = sc.nextInt()
        Arrays.sort(arr)
        q = sc.nextInt()
        for j in range(0, q):
            x = sc.nextInt()
            l = 0
            r = n - 1
            m = 0
            while l <= r:
                m = math.trunc((l + r) / float(2))
                if x >= arr [m]:
                    l = m + 1
                else:
                    r = m - 1
            print(l)
