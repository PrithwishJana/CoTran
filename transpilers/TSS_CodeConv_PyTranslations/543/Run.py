class Run:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] Z) throws IOException
    def main(Z):
        br = BufferedReader(InputStreamReader(System.in))
        op = StringBuilder()
        stz = None
        T = int(br.readLine())
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (T -- > 0)
        while T  > 0:
            T -= 1
            n = int(br.readLine())
            stz = StringTokenizer(br.readLine())
            a = [0 for _ in range(4 * n)]
            i = 0
            while i < n << 2:
                a [i] = int(stz.nextToken())
                i += 1
            yes = True
            Arrays.sort(a)
            area = a [0] * a [len(a) - 1]
            for i in range(0, n):
                lf = i * 2
                rg = 4 * n - (i * 2) - 1
                if (a [lf] != a [lf + 1]) or (a [rg] != a [rg - 1]) or (a [lf] * a [rg] != area):
                    yes = False
                    break
            if yes:
                op.append("YES\n")
            else:
                op.append("NO\n")
        T -= 1
        print(op)
