class B148:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        VP = in_.nextInt()
        VD = in_.nextInt()
        T = in_.nextInt()
        F = in_.nextInt()
        C = in_.nextInt()
        if VD <= VP:
            print("0")
            return
        answer = 0
        start = T
        while True:
            x = start * VP / (VD - VP)
            if (start + x) * VP >= C:
                break
            start += 2 * x + F
            answer += 1
        print(answer)
