import math

class Hello:
    @staticmethod
    def main(args):
        in_ = Scanner(System.in)
        pw = PrintWriter(System.out)
        n = in_.nextInt()
        square = n * n
        odd = []
        even = []
        for i in range(1, square + 1):
            if math.fmod(i, 2) == 0:
                even.append(i)
            else:
                odd.append(i)
        loop = math.trunc(square / float(n))
        div = math.trunc(loop / float(2))
        Hello.debug(div)
        for i in range(1, loop + 1):
            for j in range(0, div):
                if math.fmod(i, 2) == 1:
                    pw.print(odd.pop(0) + " " + (even.pop(len(even) - 1)) + " ")
                else:
                    pw.print(even.pop(0) + " " + (odd.pop(len(odd) - 1)) + " ")
            pw.println()
        pw.close()
    @staticmethod
    def debug(*obj):
        System.err.println(Arrays.deepToString(obj))
