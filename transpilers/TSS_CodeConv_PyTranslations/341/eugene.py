import math

class eugene:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        sc = java.util.Scanner(System.in)
        n = sc.nextInt()
        k = sc.nextInt()
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            arr [i] = sc.nextInt()
        res = StringBuffer()
        o = 0
        e = 0
        for i in range(0, n):
            if arr [i] == 1:
                o += 1
            else:
                e += 1
        for i in range(0, k):
            l = sc.nextInt()
            r = sc.nextInt()
            if math.fmod((r - l + 1), 2) == 1:
                res.append("0\n")
            else:
                if math.trunc((r - l + 1) / float(2)) <= o and math.trunc((r - l + 1) / float(2)) <= e:
                    res.append("1\n")
                else:
                    res.append("0\n")
        print(res, end = '')
        sc.close()
