class pre598:
    class FastReader:
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = None
            self.st = None

            self.br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        def next(self):
            while self.st is None or not self.st.hasMoreElements():
                try:
                    self.st = java.util.StringTokenizer(self.br.readLine())
                except java.io.IOException as e:
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
                str = self.br.readLine()
            except java.io.IOException as e:
                e.printStackTrace()
            return str
    @staticmethod
    def main(args):
        obj = FastReader()
        n = obj.nextInt()
        d = obj.nextInt()
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            arr [i] = obj.nextInt()
        arr.sort()
        max = Integer.MIN_VALUE
        for i in range(0, n):
            count = 0
            l = arr [i] + d
            for j in range(i, n):
                if l < arr [j]:
                    break
                count += 1
            max = max(max, count)
        print(n - max)
