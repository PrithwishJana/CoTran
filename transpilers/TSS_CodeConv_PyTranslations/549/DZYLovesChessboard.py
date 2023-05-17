import math

class DZYLovesChessboard:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws FileNotFoundException
    def main(args):
        in_ = FastReader()
        out = PrintWriter(BufferedOutputStream(System.out))
        n = in_.nextInt()
        m = in_.nextInt()
        arr = [['\0' for _ in range(m)] for _ in range(n)]
        for i in range(0, n):
            arr [i] = in_.nextLine().toCharArray()
        for i in range(0, n):
            w = math.fmod(i, 2) == 0
            for j in range(0, m):
                w = not w
                if arr [i][j] == '.':
                    out.print('W' if w else 'B')
                else:
                    out.print('-')
            out.println()
        out.close()
    class FastReader:
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: FastReader() throws FileNotFoundException
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = None
            self.st = None

            self.br = BufferedReader(InputStreamReader(FileInputStream("input.txt") if System.getProperty("ONLINE_JUDGE") is None else System.in))
        def next(self):
            while self.st is None or not self.st.hasMoreElements():
                try:
                    self.st = java.util.StringTokenizer(self.br.readLine())
                except IOException as e:
                    e.printStackTrace()
            return self.st.nextToken()
        def nextInt(self):
            return int(self.next())
        def nextLong(self):
            return int(self.next())
        def nextDouble(self):
            return float(self.next())
        def nextLine(self):
            str = ""
            try:
                str = self.br.readLine()
            except IOException as e:
                e.printStackTrace()
            return str
