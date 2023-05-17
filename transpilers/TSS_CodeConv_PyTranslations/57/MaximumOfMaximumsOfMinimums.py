class MaximumOfMaximumsOfMinimums:
    @staticmethod
    def main(args):
        in_ = Scanner(System.in)
        pw = PrintWriter(System.out)
        n = in_.nextInt()
        k = in_.nextInt()
        a = [0 for _ in range(n)]
        for i in range(0, n):
            a [i] = in_.nextLong()
        pw.println(MaximumOfMaximumsOfMinimums.solve(n, a, k))
        pw.close()
    @staticmethod
    def solve(n, a, k):
        if k == 1:
            res = Long.MAX_VALUE
            for x in a:
                res = min(x, res)
            return res
        if k == 2:
            if n == 1:
                return a [0]
            dq = ArrayDeque()
            for x in a:
                dq.add(x)
            lMin = Long.MAX_VALUE
            rMin = Long.MAX_VALUE
            ans = a [0]
            while not dq.isEmpty():
                lMin = min(dq.pollFirst(), lMin)
                if rMin == Long.MAX_VALUE and dq.isEmpty():
                    rMin = Long.MIN_VALUE
                    break
                if dq.isEmpty():
                    break
                rMin = Long.min(dq.getLast(), rMin)
                ans = max(ans, max(rMin, lMin))
            ans = max(ans, max(rMin, lMin))
            return ans
        ans = Long.MIN_VALUE
        for x in a:
            ans = max(ans, x)
        return ans
    @staticmethod
    def debug(*obj):
        System.err.println(Arrays.deepToString(obj))
