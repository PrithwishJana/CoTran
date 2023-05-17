class B1680:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        T = in_.nextInt()
        for t in range(0, T):
            R = in_.nextInt()
            C = in_.nextInt()
            A = [[] for _ in range(R)]
            for r in range(0, R):
                A [r] = in_.next().toCharArray()
            r = - 1
            c = - 1
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java labels and gotos:
#            outer :
            for rr in range(0, R):
                for cc in range(0, C):
                    if A [rr][cc] == 'R':
                        r = rr
                        c = cc
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java labels and gotos:
#                        break outer
            ok = True
            for rr in range(r + 1, R):
                for cc in range(0, c):
                    if A [rr][cc] == 'R':
                        ok = False
            print("YES" if ok else "NO")
