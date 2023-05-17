class JavaApplication125:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        num = sc.nextInt()
        old = - 1
        ans = 0
        for i in range(0, num):
            s = sc.nextInt()
            if s == 1:
                if old >= 0:
                    ans *= (i - old)
                else:
                    ans = 1
                old = i
        print(ans)
