class Coder:
    n = 0
    str = StringBuffer()
    a = None
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve():
        Coder.a.sort()
        cur = Coder.a[0] * 2
        i = 1
        while i < Coder.n:
            if Coder.a[i] == Coder.a[i - 1]:
                i += 1
                continue
            if Coder.a[i] < cur:
                Coder.str.append("YES\n")
                return
            cur = Coder.a[i] * 2
            i += 1
        Coder.str.append("NO\n")
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        bf = None
        pw = None
        lenv = False
        if lenv:
            bf = BufferedReader(FileReader("input.txt"))
            pw = PrintWriter(BufferedWriter(FileWriter("output.txt")))
        else:
            bf = BufferedReader(InputStreamReader(System.in))
            pw = PrintWriter(OutputStreamWriter(System.out))
        s = bf.readLine().trim().split("\\s+")
        Coder.n = int(s [0])
        Coder.a = []
        s = bf.readLine().trim().split("\\s+")
        i = 0
        while i < Coder.n:
            Coder.a.append(int(s [i]))
            i += 1
        Coder.solve()
        pw.println(Coder.str)
        pw.flush()
