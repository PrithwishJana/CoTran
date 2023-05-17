#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Integer.parseInt
class MikeandShortcuts:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        in_ = BufferedReader(InputStreamReader(System.in))
        out = StringBuilder()
        tk = None
        n = parseInt(in_.readLine())
        a = [0 for _ in range(n)]
        tk = StringTokenizer(in_.readLine())
        for i in range(0, n):
            a [i] = parseInt(tk.nextToken()) - 1
        g = [None for _ in range(n)]
        for i in range(0, n):
            g [i] = []
        i = 0
        while i < n - 1:
            if a [i] != i:
                g [i].append(a [i])
            g [i].append(i + 1)
            g [i + 1].append(i)
            i += 1
        if a [n - 1] != n - 1:
            g [n - 1].append(a [n - 1])
        dist = [0 for _ in range(n)]
        Arrays.fill(dist, - 1)
        dist [0] = 0
        q = LinkedList()
        q.add(0)
        while not q.isEmpty():
            u = q.remove()
            for v in g [u]:
                if dist [v] == - 1:
                    q.add(v)
                    dist [v] = dist [u] + 1
        out.append(dist [0])
        for i in range(1, n):
            out.append(" ").append(dist [i])
        print(out)
