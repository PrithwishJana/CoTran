class B1150:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        n = int(br.readLine())
        arr = [[None for _ in range(n)] for _ in range(n)]
        for i in range(0, n):
            line = br.readLine()
            for k in range(0, n):
                arr [i][k] = line[k] + ""
        print(B1150.solve(arr, n))
    @staticmethod
    def solve(arr, n):
        for i in range(0, n):
            for k in range(0, n):
                if arr [i][k] == ".":
                    if i + 2 < n and k + 1 < n and k - 1 >= 0:
                        if arr [i][k] == "." and arr [i + 1][k] == "." and arr [i + 1][k - 1] == "." and arr [i + 1][k + 1] == "." and arr [i + 2][k] == ".":
                            arr [i][k] = "#"
                            arr [i + 1][k] = "#"
                            arr [i + 1][k - 1] = "#"
                            arr [i + 1][k + 1] = "#"
                            arr [i + 2][k] = "#"
                        else:
                            return "NO"
                    else:
                        return "NO"
        return "YES"
