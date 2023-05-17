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
        n = obj.nextInt()
        k = obj.nextInt()
        num = obj.next().toCharArray()
        if n == 1 and k > 0:
            out.println(0)
            return
        i = 0
        while i < n and k > 0:
            if i == 0:
                if num [i] == '1':
                    i += 1
                    continue
                num [i] = '1'
                k -= 1
            else:
                if num [i] == '0':
                    i += 1
                    continue
                num [i] = '0'
                k -= 1
            i += 1
        for i in range(0, n):
            out.print(num [i])
