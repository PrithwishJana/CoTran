class program:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
    def main(args):
        sf = Scanner(System.in)
        t = 1
        for t1 in range(0, t):
            n = sf.nextInt()
            m = sf.nextInt()
            p = [0 for _ in range(n)]
            hash = [0 for _ in range(n + 1)]
            for i in range(0, n):
                p [i] = sf.nextInt()
                hash [i] = p [i]
            for i in range(0, m):
                l = sf.nextInt()
                r = sf.nextInt()
                x = sf.nextInt()
                l -= 1
                r -= 1
                x -= 1
                ind = x
                if ind < l or ind > r:
                    print("Yes")
                else:
                    hash1 = [0 for _ in range(n + 1)]
                    for j in range(0, l):
                        hash1 [p [j]] += 1
                    for j in range(r + 1, n):
                        hash1 [p [j]] += 1
                    cnt = 0
                    for j in range(1, n + 1):
                        if hash1 [j] == 0:
                            cnt += 1
                        if j == hash [x]:
                            break
                    dif1 = ind - l + 1
                    if dif1 != cnt:
                        print("No")
                    else:
                        print("Yes")
