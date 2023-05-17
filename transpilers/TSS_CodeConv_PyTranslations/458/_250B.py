class _250B(Runnable):

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._in_ = None

#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: private Object solve() throws java.io.IOException
    def _solve(self):
        sb = StringBuilder()
        i = 0
        n = nextInt()
        while i < n:
            s = self._nextToken().split(":", - 1)
            k = 0
            m = len(s) - 1
            if not s[k]:
                k += 1
            if not s[m]:
                m -= 1
            for j in range(k, m + 1):
                if not s[j]:
                    l = 1
                    lim = 8 - m + k
                    while l <= lim:
                        sb.append("0000")
                        if l < lim:
                            sb.append(':')
                        l += 1
                else:
                    for l in range(len(s[j])), 4):
                        sb.append('0')
                    sb.append(s [j])
                if j < m:
                    sb.append(':')
            sb.append('\n')
            i += 1
        return sb
    @staticmethod
    def main(args):
        (_250B()).run()
    def run(self):
        try:
            self._in_ = java.io.BufferedReader(java.io.InputStreamReader(System.in))
            print(self._solve(), end = '')
            self._in_.close()
        except java.io.IOException as e:
            System.exit(0)
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: private String nextToken() throws java.io.IOException
    def _nextToken(self):
        return self._in_.readLine()
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: private int nextInt() throws java.io.IOException
    def _nextInt(self):
        return int(self._nextToken())
