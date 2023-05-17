import math

class B:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = Scanner(System.in)
        pw = PrintWriter(System.out)
        n = in_.nextInt()
        s = in_.nextLong()
        a = [0 for _ in range(n)]
        Arrays.setAll(a, lambda i : in_.nextLong())
        pw.println(B.solve(n, a, s))
        pw.close()
    @staticmethod
    def solve(n, a, s):
        ans = - 1
        sum = 0
        r = Long.MAX_VALUE
        for i in range(0, n):
            sum += a [i]
            r = min(a [i], r)
        if sum < s:
            return - 1
        l = 0
        while l <= r:
            mid = math.trunc((l + r) / float(2))
            if B.possible(n, a, s, mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
    @staticmethod
    def possible(n, a, s, least):
        sum = 0
        for i in range(0, n):
            sum += (a [i] - least)
        if s <= sum:
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def debug(*obj):
        System.err.println(Arrays.deepToString(obj))
