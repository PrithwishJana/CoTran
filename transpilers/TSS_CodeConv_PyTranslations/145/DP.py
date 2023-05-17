class DP:
    mod = int(1e)9 + 7
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        in_ = Scanner(System.in)
        out = PrintWriter(System.out)
        N = in_.nextInt()
        dp = [0 for _ in range(1 << 3)]
        Arrays.fill(dp, Integer.MAX_VALUE)
        dp [0] = 0
        for i in range(0, N):
            price = in_.nextInt()
            s = in_.next()
            mask = 0
            if "A" in s:
                mask |= 1
            if "B" in s:
                mask |= 2
            if "C" in s:
                mask |= 4
            k = 0
            while k < (1 << 3):
                if dp [k] != Integer.MAX_VALUE:
                    t = k | mask
                    dp [t] = min(dp [t], dp [k] + price)
                k += 1
        out.println(- 1 if dp [7] == Integer.MAX_VALUE else dp [7])
        out.close()
    class Scanner:

        def _initialize_instance_fields(self):
            #instance fields found by Java to Python Converter:
            self.st = None
            self.br = None

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public Scanner(InputStream s)
        def __init__(self, s):
            self._initialize_instance_fields()

            self.br = BufferedReader(InputStreamReader(s))
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public Scanner(String s) throws FileNotFoundException
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
        def __init__(self, s):
            self._initialize_instance_fields()

            self.br = BufferedReader(FileReader(s))
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public String next() throws IOException
        def next(self):
            while self.st is None or not self.st.hasMoreTokens():
                self.st = StringTokenizer(self.br.readLine())
            return self.st.nextToken()
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public int nextInt() throws IOException
        def nextInt(self):
            return int(self.next())
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public long nextLong() throws IOException
        def nextLong(self):
            return int(self.next())
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public String nextLine() throws IOException
        def nextLine(self):
            return self.br.readLine()
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public double nextDouble() throws IOException
        def nextDouble(self):
            return float(self.next())
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public boolean ready() throws IOException
        def ready(self):
            return self.br.ready()
