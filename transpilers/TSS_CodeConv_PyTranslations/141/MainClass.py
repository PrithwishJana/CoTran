import math

class MainClass:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        st = StringTokenizer(br.readLine())
        t = int(st.nextToken())
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            st = StringTokenizer(br.readLine())
            x = int(st.nextToken())
            s = str(x)
            extra = len(s)
            temp = Character.getNumericValue(s[0])
            ans = 0
            for i in range(1, temp):
                ans += 10
            ans += math.trunc((extra) * (extra + 1) / float(2))
            print(ans)
        t -= 1
