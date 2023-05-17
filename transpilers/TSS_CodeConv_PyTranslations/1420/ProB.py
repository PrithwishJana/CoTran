class ProB:
    a = 0
    b = 0
    ans = 0
    ss = None
    aa = None
    bb = None
    mm = [0 for _ in range(200005)]
    @staticmethod
    def main(args):
        in_ = Scanner(System.in)
        ProB.ss = in_.next()
        ProB.aa = ProB.ss.toCharArray()
        ProB.a = len(ProB.ss)
        ProB.ss = in_.next()
        ProB.bb = ProB.ss.toCharArray()
        ProB.b = len(ProB.ss)
        i = 1
        while i <= ProB.b:
            ProB.mm [i] = ProB.mm [i - 1] + ProB.bb [i - 1] - '0'
            i += 1
        i = 0
        while i < ProB.a:
            if ProB.aa [i] == '0':
                ProB.ans += int(ProB.mm [ProB.b - ProB.a + i + 1]) - ProB.mm [i]
            else:
                ProB.ans += int(ProB.b) - ProB.a + 1 - (ProB.mm [ProB.b - ProB.a + i + 1] - ProB.mm [i])
            i += 1
        print(ProB.ans)
