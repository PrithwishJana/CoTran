class CF840A:
    scanner = None
    @staticmethod
    def main(args):
        CF840A.scanner = Scanner(System.in)
        n = CF840A.scanner.nextInt()
        a = []
        b = [[0 for _ in range(2)] for _ in range(n)]
        for i in range(0, n):
            a.append(int(CF840A.scanner.next()))
        for i in range(0, n):
            b [i][0] = int(CF840A.scanner.next())
            b [i][1] = i
        a.sort(Comparator.reverseOrder())
        Arrays.sort(b, ComparatorAnonymousInnerClass())
        res = [0 for _ in range(n)]
        for i in range(0, n):
            e = b [i]
            res [e [1]] = a[i]
        for i in range(0, n):
            print(str(res [i]) + " ", end = '')

    class ComparatorAnonymousInnerClass(Comparator):
        def compare(self, o1, o2):
            cmp = Integer.compare(o1 [0], o2 [0])
            if cmp == 0:
                return Integer.compare(o1 [1], o2 [1])
            else:
                return cmp
