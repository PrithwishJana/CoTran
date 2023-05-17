import math

class codforce:
    @staticmethod
    def main(args):
        str = Scanner(System.in)
        n = str.nextInt()
        s = ""
        while n > 0:
            x = math.fmod(n, 2)
            n = math.trunc(n / float(2))
            s += str(x) + ""
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == '1':
                ans += 1
            i += 1
        print(ans)
