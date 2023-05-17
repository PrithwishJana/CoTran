class akarshanand2810:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        akarshanand2810.solve()
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void solve() throws IOException
    def solve():
        sc = Reader()
        out = PrintWriter(System.out)
        n = sc.nextInt()
        arr = sc.next().toCharArray()
        cnt = 0
        idx = []
        i = 0
        while i < n - 1:
            if arr [i] == arr [i + 1]:
                cnt += 1
                idx.append(i)
            i = i + 2
        print(cnt)
        for index in idx:
            if arr [index] == 'a':
                arr [index] = 'b'
            else:
                arr [index] = 'a'
        out.println(str(arr))
        out.flush()
    class Reader:
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = None
            self.st = None

            self.br = BufferedReader(InputStreamReader(System.in))
        def next(self):
            while self.st is None or not self.st.hasMoreElements():
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
                if self.st.hasMoreTokens():
                    str = self.st.nextToken("\n")
                else:
                    str = self.br.readLine()
            except IOException as e:
                e.printStackTrace()
            return str
