class B203:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        N = in_.nextInt()
        M = in_.nextInt()
        black = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
        for m in range(1, M + 1):
            x = in_.nextInt()
            y = in_.nextInt()
            xx = x - 1
            while xx <= x + 1:
                yy = y - 1
                while yy <= y + 1:
                    black [xx][yy] += 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: if (++ black [xx][yy] == 9)
                    if  black [xx][yy] == 9:
                        print(m)
                        return
                    yy += 1
                xx += 1
        print("-1")
