class Solution788A:
    arr = [0 for _ in range(100001)]
    dist = [0 for _ in range(100001)]
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws NumberFormatException, IOException
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        n = int(br.readLine())
        st = StringTokenizer(br.readLine(), " ")
        for i in range(1, n + 1):
            Solution788A.arr [i] = int(st.nextToken())
        finalMax = 0
        for start in range(1, 3):
            max = 0
            sum = 0
            add = True
            for i in range(start, n):
                Solution788A.dist [i] = abs(Solution788A.arr [i] - Solution788A.arr [i + 1])
                if add:
                    sum += Solution788A.dist [i]
                    max = sum if sum > max else max
                    add = False
                else:
                    sum -= Solution788A.dist [i]
                    add = True
                if sum < 0:
                    sum = 0
                    add = True
            finalMax = max if max > finalMax else finalMax
        print(finalMax)
