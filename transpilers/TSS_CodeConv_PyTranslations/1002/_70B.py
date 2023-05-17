class _70B(Runnable):

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._in_ = None

#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: private Object solve() throws IOException
    def _solve(self):
        n = self._nextInt()
        c = 0
        q = 0
        s = self._nextToken()
        i = 0
        l = s.length()
        p = 0
        while i < l:
            h = s[i]
            p += 1
            if h == '.' or h == '!' or h == '?':
                if p > n:
                    return "Impossible"
                if q == 0:
                    q = p
                elif q + 1 + p <= n:
                    q += 1 + p
                else:
                    q = p
                    c += 1
                p = 0
                i += 1
            i += 1
        if q > 0:
            c += 1
        return c
    @staticmethod
    def main(args):
        (_70B()).run()
    def run(self):
        try:
            self._in_ = BufferedReader(InputStreamReader(System.in))
            out = System.out
            out.print(self._solve())
            self._in_.close()
        except IOException as e:
            System.exit(0)
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: private String nextToken() throws IOException
    def _nextToken(self):
        return self._in_.readLine()
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: private int nextInt() throws IOException
    def _nextInt(self):
        return int(self._nextToken())
