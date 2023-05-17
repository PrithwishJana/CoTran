#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static System. *
#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math. *
class pre5:
    class FastReader:

        def _initialize_instance_fields(self):
            #instance fields found by Java to Python Converter:
            self.br = None
            self.st = None

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public FastReader()
        def __init__(self):
            self._initialize_instance_fields()

            self.br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def next(self):
            while self.st is None or not self.st.hasMoreElements():
                try:
                    self.st = java.util.StringTokenizer(self.br.readLine())
                except java.io.IOException as e:
                    e.printStackTrace()
            return self.st.nextToken()
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def nextInt(self):
            return int(self.next())
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def nextLong(self):
            return int(self.next())
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def nextDouble(self):
            return float(self.next())
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def nextLine(self):
            str = ""
            try:
                str = self.br.readLine()
            except java.io.IOException as e:
                e.printStackTrace()
            return str
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        obj = FastReader()
        k = obj.nextInt()
        str = obj.next().toCharArray()
        n = len(str)
        str.sort()
        sum = 0
        for i in range(0, n):
            sum += (str [i] - '0')
        idx = 0
        ans = 0
        while idx < n and sum < k:
            sum -= str [idx] - '0'
            str [idx] = '9'
            sum += 9
            idx += 1
            ans += 1
        out.println(ans)
