class Codechef:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        scan = Scanner(System.in)
        T = scan.nextInt()
        for i in range(0, T):
            s = scan.next()
            len = len(s)
            if len == 1:
                print("NO")
                continue
            count = 1
            a = True
            j = 0
            while j < len - 1:
                if s[j] == s[j + 1]:
                    count += 1
                else:
                    if count == 1:
                        a = False
                        break
                    elif j == len - 2:
                        a = False
                    else:
                        count = 1
                j += 1
            if a == True:
                print("YES")
            else:
                print("NO")
