import math

class ex8:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        sc.nextLine()
        count = 0
        flag = 0
        s = [None for _ in range(n)]
        for i in range(0, n):
            s [i] = " " + sc.nextLine()
        for i in range(0, n):
            res = ""
            count = 0
            for q in range(1, 13):
                if s [i].charAt(q) == 'X':
                    res = " 1x12"
                    count += 1
                    break
            for j in range(2, 7):
                flag = 0
                if math.fmod(12, j) == 0:
                    k = 1
                    while k <= math.trunc(12 / float(j)):
                        flag = 0
                        for p in range(k, 13, math.trunc(12 / float(j))):
                            if s [i].charAt(p) == 'O':
                                flag = 1
                                break
                        if flag == 0:
                            count += 1
                            res += " " + str(j) + "x" + math.trunc(12 / float(j))
                            break
                        k += 1
            flag = 0
            for l in range(1, 13):
                if s [i].charAt(l) == 'O':
                    flag = 1
                    break
            if flag == 0:
                res += " 12x1"
                count += 1
            print("{0:d}{1}".format(count, res), end = '')
            print()
