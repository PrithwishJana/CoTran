import math

class B1593:
    @staticmethod
    def main(args):
        scanner = java.util.Scanner(System.in)
        t = scanner.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            s = scanner.next()
            ans = 0
            list = java.util.LinkedList()
            for i in range(len(s) - 1, -1, -1):
                ch = s[i]
                if len(list) == 0:
                    if ch == '0' or ch == '5':
                        list.append(ch + "")
                    else:
                        ans += 1
                else:
                    found = False
                    for str in list:
                        if math.fmod(int(ch + str), 25) == 0:
                            found = True
                            ans += len(list) - 1
                            break
                    if found:
                        break
                    if ch == '0' or ch == '5':
                        list.append(ch + "")
                    else:
                        ans += 1
            print(ans)
        t -= 1
        scanner.close()
