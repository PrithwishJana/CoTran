import math

class evenSum:
    br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
    pw = java.io.PrintWriter(System.out)
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException, InterruptedException
    def main(args):
        n = int(evenSum.br.readLine() + "")
        max = 0
        s = evenSum.br.readLine()
        x = s.split(" ")
        even = list(n)
        odd = list(n)
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (n -- > 0)
        while n  > 0:
            n -= 1
            y = int(x [n])
            if math.fmod(y, 2) == 0:
                even.append(y)
            else:
                odd.append(y)
        n -= 1
        for i, unusedItem in enumerate(even):
            max += even[i]
        odd2 = [0 for _ in range(len(odd))]
        for i, unusedItem in enumerate(odd):
            odd2 [i] = odd[i]
        Arrays.sort(odd2)
        for i in range(len(odd2) - 1, 0, -1):
            max += odd2 [i]
        if math.fmod(len(odd2), 2) == 0 and len(odd2) > 0:
            max += odd2 [0]
        evenSum.pw.println(max)
        evenSum.pw.close()
