import math

class Another:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        in_ = FastReader()
        pw = java.io.PrintWriter(System.out)
        m = in_.nextLong()
        R = in_.nextLong()
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        pw.printf("%.12f\n", (2 + 2.0 * (m - 1) * m * (m + 1) / 3 / m / m - 2 * (2 - math.sqrt(2)) + (2 - math.sqrt(2)) * (2 * m + 2 * (m - 1)) / m / m) * R)
        pw.flush()
        pw.close()
    class FastReader:
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.st = None
            self.br = None

            self.br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public String next() throws java.io.IOException
        def next(self):
            if self.st is None or not self.st.hasMoreTokens():
                self.st = java.util.StringTokenizer(self.br.readLine())
            return self.st.nextToken()
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public boolean hasNext() throws java.io.IOException
        def hasNext(self):
            if self.st is not None and self.st.hasMoreTokens():
                return True
            s = self.br.readLine()
            if s is None or not s:
                return False
            self.st = java.util.StringTokenizer(s)
            return True
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public int nextInt() throws java.io.IOException
        def nextInt(self):
            return int(self.next())
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public long nextLong() throws java.io.IOException
        def nextLong(self):
            return int(self.next())
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public double nextDouble() throws java.io.IOException
        def nextDouble(self):
            return float(self.next())
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public String nextLine() throws java.io.IOException
        def nextLine(self):
            return self.br.readLine()
