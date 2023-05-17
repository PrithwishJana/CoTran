class okabeandfuturegadgetlaboratory:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        fin = BufferedReader(InputStreamReader(System.in))
        n = int(fin.readLine())
        lab = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(0, n):
            st = StringTokenizer(fin.readLine())
            for j in range(0, n):
                lab [i][j] = int(st.nextToken())
        ans = True
        for x in range(0, n):
            for y in range(0, n):
                if lab [x][y] != 1:
                    cur = lab [x][y]
                    isValid = False
                    for i in range(0, n):
                        for j in range(0, n):
                            if lab [x][i] + lab [j][y] == cur:
                                isValid = True
                                break
                        if isValid:
                            break
                    if not isValid:
                        ans = False
                        break
            if not ans:
                break
        print("Yes" if ans else "No")
