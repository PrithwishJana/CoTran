class ER42B:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        n = in_.nextInt()
        a = in_.nextInt()
        b = in_.nextInt()
        s = in_.next()
        ans = a + b
        flip = 1 if a > b else - 1
        for i in range(0, n):
            if a == 0 and b == 0:
                break
            if s[i] == '*':
                flip = 1 if a > b else - 1
            else:
                if flip == 1:
                    a = (0 if a == 0 else a - 1)
                else:
                    b = (0 if b == 0 else b - 1)
                flip *= - 1
        print(ans - a - b)
