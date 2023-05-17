import math

class A:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.in_ = None

    _MOD = 1000003
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        reader = BufferedReader(InputStreamReader(System.in))
        writer = PrintWriter(BufferedWriter(OutputStreamWriter(System.out)))
        n = int(reader.readLine())
        ans = 1 if n == 0 else A.pow(3, n - 1, A._MOD)
        writer.println(ans)
        reader.close()
        writer.close()
    @staticmethod
    def pow(a, p, m):
        if p == 0:
            return math.fmod(int(1), m)
        if p == 1:
            return math.fmod(int(a), m)
        v = A.pow(a, math.trunc(p / float(2)), m)
        ans = math.fmod(v * v, m)
        if math.fmod(p, 2) == 1:
            ans = math.fmod(ans * a, m)
        return ans
