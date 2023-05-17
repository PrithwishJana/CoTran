import math

class EhabOddPerson:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws NumberFormatException, IOException
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        n = int(br.readLine().trim())
        line1 = br.readLine().trim().split(" ")
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            arr [i] = int(line1 [i])
        odd = False
        even = False
        ans = []
        for i in range(0, n):
            if math.fmod(arr [i], 2) == 0:
                even = True
            else:
                odd = True
            ans.append(arr [i])
        if odd and even:
            ans.sort()
        for i in range(0, n):
            print(ans[i])
