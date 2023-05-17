class practice462b:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws Exception
    def main(args):
        f = BufferedReader(InputStreamReader(System.in))
        out = PrintWriter(BufferedWriter(OutputStreamWriter(System.out)))
        st = StringTokenizer(f.readLine())
        n = int(st.nextToken())
        k = int(st.nextToken())
        cards = [None for _ in range(26)]
        for i in range(0, 26):
            cards [i] = c462b()
        s = f.readLine()
        for t in range(0, n):
            cards [s[t] - 'A'].left += 1
        ans = 0
        i = 0
        while i < k:
            Arrays.sort(cards)
            change = min(cards [25].left, k - i)
            ans += change * change
            cards [25].left -= change
            i += change - 1
            i += 1
        out.println(ans)
        out.close()
class c462b(Comparable):

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.left = 0

    def compareTo(self, o):
        return self.left - (o).left
