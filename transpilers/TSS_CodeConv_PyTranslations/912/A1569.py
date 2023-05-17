class A1569:
    flag = False
    finals = 0
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        cases = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (cases -- > 0)
        while cases  > 0:
            cases -= 1
            A1569.flag = False
            letters = sc.nextInt()
            ab = sc.next()
            for i in range(1, letters):
                if ab[i - 1] != ab[i]:
                    A1569.flag = True
                    print(str(i) + " " + str(i + 1))
                    break
            if A1569.flag == False:
                print("-1 " + "-1")
        cases -= 1
