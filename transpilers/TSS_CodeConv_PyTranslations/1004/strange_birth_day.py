class strange_birth_day:
    def helpBirthDayBoy(self, n, m):
        Arrays.sort(n)
        ans = 0
        j = 0
        for i in range(len(n) - 1, -1, -1):
            k = n [i]
            if k < len(m):
                if m [k] > m [j]:
                    ans += m [j]
                    j += 1
                else:
                    ans += m [k]
        print(ans)
    @staticmethod
    def main(args):
        in_ = FastReader()
        test = in_.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (test -- > 0)
        while test  > 0:
            test -= 1
            n = in_.nextInt()
            m = in_.nextInt()
            arr = [0 for _ in range(n)]
            marr = [0 for _ in range(m)]
            for i in range(0, n):
                arr [i] = in_.nextInt() - 1
            for i in range(0, m):
                marr [i] = in_.nextInt()
            strange = strange_birth_day()
            strange.helpBirthDayBoy(arr, marr)
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
