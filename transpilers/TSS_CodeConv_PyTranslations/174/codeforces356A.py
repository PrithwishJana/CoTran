class codeforces356A:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws Exception
    def main(args):
        in_ = FastReader()
        n = in_.nextInt()
        left = TreeSet()
        answer = [0 for _ in range(n)]
        for i in range(0, n):
            left.add(i)
        q = in_.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (q -- > 0)
        while q  > 0:
            q -= 1
            l = in_.nextInt() - 1
            r = in_.nextInt() - 1
            win = in_.nextInt()
            while left.ceiling(l) is not None and left.ceiling(l) <= r:
                curr = left.ceiling(l)
                answer [curr] = win
                left.remove(curr)
            answer [win - 1] = 0
            left.add(win - 1)
        q -= 1
        ans = StringBuilder()
        for i in range(0, n):
            ans.append(str(answer [i]) + " ")
        print(ans)
    class FastReader:
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.st = None
            self.br = None

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
            s = ""
            while self.st is None or self.st.hasMoreElements():
                try:
                    s = self.br.readLine()
                except IOException as e:
                    e.printStackTrace()
            return s
