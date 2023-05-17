class Algorithm:
    ans = 0
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] rgs) throws java.io.IOException
    def main(rgs):
        bufferedReader = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        stringBuilder = StringBuilder()
        t = int(bufferedReader.readLine())
        for i in range(0, t):
            a = bufferedReader.readLine().split(" ")
            row = int(a [0])
            col = int(a [1])
            ans = StringBuilder()
            ansarray = [0 for _ in range(row * col)]
            p = 0
            rowarray = [0, 0, row - 1, row - 1]
            colarray = [0, col - 1, 0, col - 1]
            for j in range(0, row):
                for k in range(0, col):
                    dis = 0
                    for l in range(0, 4):
                        dis = max(dis, abs(rowarray [l] - j) + abs(colarray [l] - k))
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: ansarray [p ++] = dis;
                    ansarray [p ] = dis
                    p += 1
            ansarray.sort()
            j = 0
            while j < len(ansarray):
                ans.append(ansarray [j]).append(" ")
                j += 1
            stringBuilder.append(ans).append("\n")
        print(stringBuilder)
