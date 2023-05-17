class Practice:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- != 0)
        while t  != 0:
            t -= 1
            n = sc.nextInt()
            a = sc.nextInt()
            b = sc.nextInt()
            c = sc.nextInt()
            d = sc.nextInt()
            flag = False
            k = n * (a - b)
            m = n * (a + b)
            if k > (c + d) or m < (c - d):
                print("NO")
            else:
                print("YES")
        t -= 1
