import math

#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Long.max
#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Long.toHexString
#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math.abs
#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math.sin
class B:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = MyScanner()
        m = in_.nextInt()
        b = in_.nextInt()
        result = 0
        x = 1
        while x <= m * b:
            y = int((- 1.0 * x / m + b))
            result = max(result, math.trunc(1 * (x + 1) * (y) * (y + 1) / float(2)) + math.trunc(1 * (y + 1) * (x) * (x + 1) / float(2)))
            x += 1
        print(result)
    class MyScanner:
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.br = None
            self.st = None

            self.br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        def next(self):
            while self.st is None or not self.st.hasMoreElements():
                try:
                    self.st = StringTokenizer(self.br.readLine())
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
