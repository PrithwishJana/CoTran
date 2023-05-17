class A1452:
    @staticmethod
    def main(args):
        scanner = java.util.Scanner(System.in)
        t = scanner.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            a = [0 for _ in range(2)]
            a [0] = scanner.nextInt()
            a [1] = scanner.nextInt()
            a.sort()
            if a [0] == a [1]:
                print(2 * a [0])
            else:
                print(2 * a [1] - 1)
        t -= 1
        scanner.close()
