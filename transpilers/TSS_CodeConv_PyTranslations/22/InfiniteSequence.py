import math

class InfiniteSequence:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        n1 = int(br.readLine())
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        n = int(((math.sqrt(1 + (8 * n1)) - 1) / 2))
        ans = n1 - (math.trunc(((n + 1) * n) / float(2)))
        print(ans if (ans != 0) else n, end = '')
