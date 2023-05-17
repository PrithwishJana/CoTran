class cf1672b:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            s = sc.next()
            a = 0
            b = 0
            f = True
            for ch in s.toCharArray():
                if ch == 'A':
                    a += 1
                else:
                    b += 1
                    if a < b:
                        print("NO")
                        f = False
                        break
            if f:
                if b != 0 and s[len(s) - 1] == 'B':
                    print("YES")
                else:
                    print("NO")
        t -= 1
