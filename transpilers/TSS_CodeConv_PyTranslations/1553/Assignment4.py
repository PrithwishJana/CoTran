import math

class Assignment4:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        str = br.readLine()
        num = str.split(" ")
        n = float(num [0])
        h = float(num [1])
        for i in range(1.0, n):
            ans = h * math.sqrt(i / n)
            print("{0:f} ".format(ans), end = '')
            if i == n - 1:
                print()
