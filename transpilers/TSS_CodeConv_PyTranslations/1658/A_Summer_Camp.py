#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math.ceil
class A_Summer_Camp:
    in_ = java.io.BufferedReader(java.io.InputStreamReader(System.in))
    out = java.io.PrintWriter(System.out)
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        n = int(A_Summer_Camp.in_.readLine())
        s = ""
        for i in range(1, n + 1):
            s += i
        A_Summer_Camp.out.print(s[n - 1])
        A_Summer_Camp.out.close()
