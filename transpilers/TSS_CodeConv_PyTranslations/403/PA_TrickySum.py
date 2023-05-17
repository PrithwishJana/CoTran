import math

class PA_TrickySum:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        reader = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        writer = java.io.BufferedWriter(java.io.OutputStreamWriter(System.out))
        t = int(reader.readLine())
        sum = 0
        valu = 0
        result = 0
        for p in range(0, t):
            n1 = int(reader.readLine())
            sum = math.trunc(n1 * (n1 + 1) / float(2))
            i = 1
            while i < n1 + 1:
                valu += i
                i = int(i) * 2
            result = sum - (valu * 2)
            writer.write("" + str(result))
            writer.newLine()
            valu = 0
        writer.newLine()
        writer.flush()
