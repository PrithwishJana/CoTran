class problem1455b:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            x = sc.nextInt()
            val = 0
            turn = 0
            while val < x:
                val += turn + 1
                turn += 1
            if val == x:
                print(turn)
            elif val == x + 1:
                print(turn + 1)
            else:
                print(turn)
        t -= 1
