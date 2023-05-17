class binary_removal:
    @staticmethod
    def remove(s):
        one = 0
        zero = 0
        i = 1
        while i < len(s):
            if s[i] == '1':
                if s[i - 1] == '1':
                    one += 1
            else:
                if s[i - 1] == '0' and one > 0:
                    print("No")
                    return
            i += 1
        print("YES")
    @staticmethod
    def main(args):
        in_ = FastReader()
        out = FastWriter()
        test = in_.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (test -- > 0)
        while test  > 0:
            test -= 1
            s = in_.nextLine()
            binary_removal.remove(s)
        test -= 1
    class FastReader:
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = None
            self.st = None

            self.br = BufferedReader(InputStreamReader(System.in))
        def next(self):
            while self.st is None or not self.st.hasMoreTokens():
                try:
                    self.st = StringTokenizer(self.br.readLine())
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
                str = self.br.readLine().trim()
            except Exception as e:
                e.printStackTrace()
            return str
    class FastWriter:
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self._bw = None

            self._bw = BufferedWriter(OutputStreamWriter(System.out))
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public void print(Object object) throws IOException
        def print(self, object):
            self._bw.append("" + object)
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public void println(Object object) throws IOException
        def println(self, object):
            self.print(object)
            self._bw.append("\n")
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public void close() throws IOException
        def close(self):
            self._bw.close()
