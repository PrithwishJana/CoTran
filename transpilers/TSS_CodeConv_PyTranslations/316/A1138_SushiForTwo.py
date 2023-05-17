class A1138_SushiForTwo:
    @staticmethod
    def main(args):
        scanner = java.util.Scanner(System.in)
        n = scanner.nextInt()
        len = 1
        prev = 0
        oneSeq = 0
        twoSeq = 0
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (n -- > 0)
        while n  > 0:
            n -= 1
            x = scanner.nextByte()
            if x == 1:
                if prev == 1:
                    oneSeq += 1
                else:
                    oneSeq = 1
                prev = 1
            else:
                if prev == 2:
                    twoSeq += 1
                else:
                    twoSeq = 1
                prev = 2
            if min(oneSeq, twoSeq) > len:
                len = min(oneSeq, twoSeq)
        n -= 1
        print(len * 2)
