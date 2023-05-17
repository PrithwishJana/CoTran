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
            a = sc.nextInt()
            b = sc.nextInt()
            c = sc.nextInt()
            if a == b and c == b:
                print(0)
            else:
                sum = abs(a - b) + abs(b - c) + abs(c - a)
                sum -= 4
                print(max(sum, 0))
        t -= 1
