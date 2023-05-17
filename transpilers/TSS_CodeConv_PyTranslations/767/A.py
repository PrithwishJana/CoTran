class A:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.in_ = None

    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = java.util.Scanner(System.in)
        cases = sc.nextInt()
        for caze in range(1, cases + 1):
            N = sc.nextInt()
            L = sc.nextInt()
            need = java.util.HashSet()
            have = java.util.HashSet()
            for i in range(0, N):
                tmp = sc.next()
                tmp2 = 0
                for j in range(0, L):
                    if tmp[j] == '1':
                        tmp2 |= (1 << j)
                have.add(tmp2)
            lastNeeded = 0
            for i in range(0, N):
                tmp = sc.next()
                tmp2 = 0
                for j in range(0, L):
                    if tmp[j] == '1':
                        tmp2 |= (1 << j)
                need.add(tmp2)
                lastNeeded = tmp2
            ans = L + 1
            for elem in have:
                flip = lastNeeded ^ elem
                got = java.util.HashSet()
                for e in need:
                    got.add(e ^ flip)
                if got is have:
                    ans = min(ans, Long.bitCount(flip))
            print("Case #" + str(caze) + ": " + ("NOT POSSIBLE" if ans > L else ans))
