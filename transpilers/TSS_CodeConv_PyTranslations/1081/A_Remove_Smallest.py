class A_Remove_Smallest:
    @staticmethod
    def main(args):
        sn = java.util.Scanner(System.in)
        t = sn.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = sn.nextInt()
            arr = [0 for _ in range(n)]
            for i in range(0, n):
                arr [i] = sn.nextInt()
            arr.sort()
            i = 0
            i = 0
            while i < n - 1:
                if (arr [i + 1] - arr [i]) <= 1:
                    i += 1
                    continue
                else:
                    break
                i += 1
            if i == n - 1:
                print("YES")
            else:
                print("NO")
        t -= 1
