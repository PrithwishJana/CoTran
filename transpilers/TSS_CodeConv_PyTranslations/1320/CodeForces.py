class CodeForces:
    BUFFERSIZE = 512000
    _sc = Scanner(BufferedReader(InputStreamReader(System.in), BUFFERSIZE))
    _out = PrintWriter(BufferedOutputStream(System.out, BUFFERSIZE))
    @staticmethod
    def solve():
        n = CodeForces._sc.nextInt()
        map = {}
        for i in range(0, n):
            map[CodeForces._sc.nextInt()] = i
        lastLoc = map[1]
        ans = 0
        for i in range(1, n + 1):
            newLoc = map[i]
            ans += abs(lastLoc - newLoc)
            lastLoc = newLoc
        CodeForces._out.println(ans)
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String args []) throws Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_.init(System.in)
        CodeForces.solve()
        CodeForces._out.close()
    class in_:
        reader = None
        tokenizer = None
        @staticmethod
        def init(input):
            CodeForces.in_.reader = BufferedReader(InputStreamReader(input), CodeForces.BUFFERSIZE)
            CodeForces.in_.tokenizer = StringTokenizer("")
        @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: static String next() throws IOException
        def next():
            while not CodeForces.in_.tokenizer.hasMoreTokens():
                CodeForces.in_.tokenizer = StringTokenizer(CodeForces.in_.reader.readLine())
            return CodeForces.in_.tokenizer.nextToken()
        @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: static int nextInt() throws IOException
        def nextInt():
            return int(CodeForces.in_.next())
        @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: static double nextDouble() throws IOException
        def nextDouble():
            return float(CodeForces.in_.next())
        @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: static long nextLong() throws IOException
        def nextLong():
            return int(CodeForces.in_.next())
