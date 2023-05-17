import math

class BinaryStr:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        bf = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        t = int(bf.readLine())
        for i in range(0, t):
            n = int(bf.readLine())
            arr = bf.readLine().toCharArray()
            arr2 = ['\0' for _ in range(n)]
            j = 0
            while j <= n - 1:
                arr2 [j] = arr [j]
                j += 1
            j = 0
            while j <= n - 1:
                if math.fmod(j, 2) == 0:
                    arr2 [j] = '0'
                else:
                    arr2 [j] = '1'
                j += 1
            cur = 0
            k = 0
            j = 0
            while j <= n - 1:
                if arr [j] == arr2 [j]:
                    j += 1
                    continue
                k = j
                while k <= n - 1:
                    if arr [k] == arr2 [k]:
                        break
                    k += 1
                cur += 1
                j = k - 1
                j += 1
            ans = Integer.MAX_VALUE
            ans = min(ans, cur)
            j = 0
            while j <= n - 1:
                if math.fmod(j, 2) == 1:
                    arr2 [j] = '0'
                else:
                    arr2 [j] = '1'
                j += 1
            cur = 0
            j = 0
            while j <= n - 1:
                if arr [j] == arr2 [j]:
                    j += 1
                    continue
                k = j
                while k <= n - 1:
                    if arr [k] == arr2 [k]:
                        break
                    k += 1
                cur += 1
                j = k - 1
                j += 1
            ans = min(ans, cur)
            print(ans)
