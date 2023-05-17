import math

class CP:
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

            self.br = BufferedReader(InputStreamReader(FileInputStream(s)))
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
    @staticmethod
    def _gcd(a, b):
        if b == 0:
            return a
        return CP._gcd(b, math.fmod(a, b))
    @staticmethod
    def _printArrayList(al):
        for i in al:
            print(i + " ", end = '')
        print()
    @staticmethod
    def _digitSum(n):
        sum = 0
        while n != 0:
            sum += math.fmod(n, 10)
            n = math.trunc(n / float(10))
        return sum
    @staticmethod
    def main(args):
        try:
            s = Scanner(System.in)
            sb = StringBuffer()
            st = s.next()
            k = s.nextInt()
            hs = HashSet()
            for x in st.toCharArray():
                hs.add(x)
            if len(st) < k:
                sb.append("impossible")
            else:
                if k <= hs.size():
                    sb.append("0\n")
                else:
                    sb.append(k - hs.size())
            print(sb)
        except Exception as e:
            print(e)
