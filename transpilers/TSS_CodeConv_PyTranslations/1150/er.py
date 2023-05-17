class er:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        out = PrintWriter(OutputStreamWriter(System.out))
        solver = TaskB()
        solver.solve(br, out)
        out.close()
class TaskB:
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public void solve(BufferedReader br, PrintWriter out) throws IOException
    def solve(self, br, out):
        st = java.util.StringTokenizer(br.readLine())
        n = int(st.nextToken())
        a = [0 for _ in range(n + 1)]
        sumA = [0 for _ in range(n + 1)]
        sumB = [0 for _ in range(n + 1)]
        a [0] = sumA [0] = sumB [0] = int(0)
        st = java.util.StringTokenizer(br.readLine())
        for i in range(1, n + 1):
            a [i] = int(st.nextToken())
            sumA [i] = sumA [i - 1] + a [i]
        a.sort()
        for i in range(1, n + 1):
            sumB [i] = sumB [i - 1] + a [i]
        st = java.util.StringTokenizer(br.readLine())
        m = int(st.nextToken())
        for i in range(0, m):
            st = java.util.StringTokenizer(br.readLine())
            type = int(st.nextToken())
            l = int(st.nextToken())
            r = int(st.nextToken())
            if type == 1:
                out.println(sumA [r] - sumA [l - 1])
            else:
                out.println(sumB [r] - sumB [l - 1])
