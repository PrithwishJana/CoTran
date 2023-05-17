class er:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        pw = PrintWriter(OutputStreamWriter(System.out))
        f = Fast()
        f.sol(br, pw)
        pw.close()
class Fast:
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public void sol(BufferedReader br, PrintWriter pw) throws IOException
    def sol(self, br, pw):
        st = java.util.StringTokenizer(br.readLine())
        s = st.nextToken()
        cum = [0 for _ in range(len(s) + 1)]
        cum [0] = cum [len(s)] = 0
        i = 1
        while i < len(s):
            if s[i] == s[i - 1]:
                cum [i] = cum [i - 1] + 1
            else:
                cum [i] = cum [i - 1]
            i += 1
        st = java.util.StringTokenizer(br.readLine())
        q = int(st.nextToken())
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (q -- != 0)
        while q  != 0:
            q -= 1
            st = java.util.StringTokenizer(br.readLine())
            l = int(st.nextToken())
            r = int(st.nextToken()) - 1
            pw.println(cum [r] - cum [l - 1])
        q -= 1
