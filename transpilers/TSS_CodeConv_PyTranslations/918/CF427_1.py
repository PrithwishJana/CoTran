import math

class CF427_1:
    N = 0
    MOD = int((1e9 + 7))
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        out = java.io.PrintWriter(System.out)
        t = in_.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = in_.nextInt()
            a = in_.nextInt()
            b = in_.nextInt()
            if n < a:
                out.println("No")
                continue
            if a == b:
                if math.fmod(n, a) == 0:
                    out.println("Yes")
                else:
                    out.println("No")
                continue
            x = math.trunc(b / float(b - a))
            if n > x * a:
                out.println("Yes")
                continue
            low = 1
            high = x + 1
            ans = 1
            while low <= high:
                mid = math.trunc((low + high) / float(2))
                if mid * a < n:
                    low = mid + 1
                else:
                    ans = mid
                    high = mid - 1
            if n > (ans - 1) * b and n < ans * a:
                out.println("No")
            else:
                out.println("Yes")
        t -= 1
        out.close()
