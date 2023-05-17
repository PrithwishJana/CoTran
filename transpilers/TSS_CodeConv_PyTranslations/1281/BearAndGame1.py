class BearAndGame1:
    @staticmethod
    def main(args):
        sc = InputReader(System.in)
        n = sc.nextInt()
        array = [0 for _ in range(100)]
        for i in range(0, n):
            array [i] = sc.nextInt()
        flag = 15
        for i in range(0, n):
            if array [i] <= flag:
                flag = array [i] + 15
            else:
                break
        result = min(flag, 90)
        outputStream = System.out
        out = PrintWriter(outputStream)
        out.println(result)
        out.close()
    class InputReader:
        def __init__(self, stream):
            #instance fields found by Java to Python Converter:
            self.reader = None
            self.tokenizer = None

            self.reader = BufferedReader(InputStreamReader(stream))
            self.tokenizer = None
        def next(self):
            while self.tokenizer is None or not self.tokenizer.hasMoreTokens():
                try:
                    self.tokenizer = java.util.StringTokenizer(self.reader.readLine())
                except IOException as e:
                    raise RuntimeException(e)
            return self.tokenizer.nextToken()
        def nextInt(self):
            return int(self.next())
        def nextDouble(self):
            return float(self.next())
