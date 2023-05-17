class CF_1712_A:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = sc.nextInt()
            k = sc.nextInt()
            a = [0 for _ in range(n)]
            for i in range(0, n):
                a [i] = sc.nextInt()
            counter = 0
            for i in range(k, n):
                if a [i] <= k:
                    counter += 1
            print(counter)
        t -= 1
