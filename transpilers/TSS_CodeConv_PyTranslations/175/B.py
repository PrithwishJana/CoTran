class B:
    set = None
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = Scanner(System.in)
        pw = PrintWriter(System.out)
        n = in_.nextInt()
        a = [0 for _ in range(n)]
        for i in range(0, n):
            a [i] = in_.nextLong()
        dp = [0 for _ in range(n + 1)]
        Arrays.fill(dp, - 1)
        dp [n - 1] = a [n - 1]
        for i in range(n - 1, -1, -1):
            dp [i] = max(dp [i + 1], a [i])
        for i in range(0, n):
            if a [i] > dp [i + 1]:
                pw.print(str(0) + " ")
            else:
                pw.print(str(dp [i + 1] - a [i] + 1) + " ")
        pw.println()
        pw.close()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def debug(*obj):
        System.err.println(Arrays.deepToString(obj))
