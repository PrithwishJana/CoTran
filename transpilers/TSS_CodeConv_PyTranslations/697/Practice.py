class Practice:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = java.util.Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = sc.nextInt()
            m = sc.nextInt()
            a = [0 for _ in range(n)]
            for i in range(0, n):
                a [i] = sc.nextInt()
            if n > m:
                print("NO")
                continue
            a.sort()
            ans = a [n - 1]
            for i in range(n - 1, -1, -1):
                ans += 1
                if i > 0:
                    ans += a [i]
            if ans <= m:
                print("YES")
            else:
                print("NO")
        t -= 1
