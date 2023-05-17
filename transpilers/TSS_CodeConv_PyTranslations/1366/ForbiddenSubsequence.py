class ForbiddenSubsequence:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        pw = java.io.PrintWriter(System.out)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            alph = [0 for _ in range(26)]
            s = sc.next()
            abc = sc.next()
            i = 0
            while i < len(s):
                alph [s[i] - 'a'] += 1
                i += 1
            if abc == "abc" and (alph [0] > 0 and alph [1] > 0 and alph [2] > 0):
                res = StringBuilder()
                i = 0
                while i < 26:
                    if i == 1:
                        while alph [2] > 0:
                            res.append(chr((2 + 'a')))
                            alph [2] -= 1
                        while alph [1] > 0:
                            res.append(chr((1 + 'a')))
                            alph [1] -= 1
                        i += 1
                    else:
                        while alph [i] > 0:
                            res.append(chr((i + 'a')))
                            alph [i] -= 1
                    i += 1
                pw.println(res)
            else:
                res = StringBuilder()
                for i in range(0, 26):
                    while alph [i] > 0:
                        res.append(chr((i + 'a')))
                        alph [i] -= 1
                pw.println(res)
        t -= 1
        pw.flush()
