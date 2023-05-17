class class6:
    @staticmethod
    def main(arg):
        sc = Scanner(System.in)
        n = sc.nextInt()
        ch = ['\0' for _ in range(n)]
        s1 = 0
        s2 = 0
        i = 0
        j = 0
        flag = 0
        dif = 0
        for i in range(0, n):
            x = sc.nextInt()
            y = sc.nextInt()
            temp1 = s1 + x
            temp2 = s2 + y
            if abs(temp1 - s2) <= 500:
                s1 += x
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: ch [j ++] = 'A';
                ch [j ] = 'A'
                j += 1
                continue
            if abs(temp2 - s1) <= 500:
                s2 += y
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: ch [j ++] = 'G';
                ch [j ] = 'G'
                j += 1
                continue
            flag = 1
            break
        if flag == 1:
            print(- 1)
        else:
            ans = ""
            ans = ans.valueOf(ch)
            print(ans)
