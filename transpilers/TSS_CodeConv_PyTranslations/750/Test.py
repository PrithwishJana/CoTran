class Test:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = sc.nextInt()
            arr = [0 for _ in range(n)]
            for i in range(0, n):
                arr [i] = sc.nextInt()
            curr = arr [n - 1]
            c = 0
            for i in range(n - 2, -1, -1):
                if arr [i] <= curr:
                    curr = arr [i]
                else:
                    c += 1
            print(c)
        t -= 1
