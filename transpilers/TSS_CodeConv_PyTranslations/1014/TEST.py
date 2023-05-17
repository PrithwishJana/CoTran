class TEST:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        T = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (T -- > 0)
        while T  > 0:
            T -= 1
            n = sc.nextInt()
            c = sc.next().toCharArray()
            del_ = n - 1
            for i in range(0, n):
                if c [i] == '>' or c [n - 1 - i] == '<':
                    print(i)
                    break
        T -= 1
