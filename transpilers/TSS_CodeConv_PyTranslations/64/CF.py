class CF:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = Scanner(System.in)
        pw = PrintWriter(System.out)
        even = in_.nextInt()
        odd = in_.nextInt()
        if even == 0 and odd == 0:
            pw.println("NO")
        else:
            sub = abs(even - odd)
            if sub <= 1:
                pw.println("YES")
            else:
                pw.println("NO")
        pw.close()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def debug(*obj):
        System.err.println(Arrays.deepToString(obj))
