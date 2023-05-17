class CF709A:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        n = sc.nextInt()
        b = sc.nextInt()
        d = sc.nextInt()
        a = 0
        sum = 0
        count = 0
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (n -- > 0)
        while n  > 0:
            n -= 1
            a = sc.nextInt()
            if a <= b:
                sum += a
            if sum > d:
                sum = 0
                count += 1
        n -= 1
        print(count)
        sc.close()
