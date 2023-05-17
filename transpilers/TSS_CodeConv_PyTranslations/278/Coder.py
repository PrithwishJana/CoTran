import math

class Coder:
    str = StringBuffer()
    n = 0
    a = None
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve():
        mx = 0
        i = 0
        while i < Coder.n:
            mx = max(Coder.a [i], mx)
            i += 1
        cnt = {}
        i = 0
        while i < Coder.n:
            cnt[Coder.a [i]] = cnt.getOrDefault(Coder.a [i], 0) + 1
            i += 1
        if math.fmod(cnt[mx], 2) != 0:
            return "Conan\n"
        elif cnt[mx] == Coder.n:
            return "Agasa\n"
        else:
            for me in cnt.entrySet():
                if math.fmod(me.getValue(), 2) != 0:
                    return "Conan\n"
            return "Agasa\n"
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
        Coder.a = [0 for _ in range(Coder.n)]
        s = bf.readLine().trim().split("\\s+")
        i = 0
        while i < Coder.n:
            Coder.a [i] = int(s [i])
            i += 1
        Coder.str.append(Coder.solve()).append("\n")
        pw.print(Coder.str)
        pw.flush()
