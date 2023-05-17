import math

class compititive_programmer:
    @staticmethod
    def main(args):
        t = 0
        in_ = Scanner(System.in)
        t = in_.nextInt()
        in_.nextLine()
        while t != 0:
            t -= 1
            s = in_.nextLine()
            zero = 0
            sum = 0
            even = 0
            i = 0
            while i < len(s):
                sum += (s[i] - '0')
                if s[i] == '0':
                    zero += 1
                if math.fmod(s[i], 2) == 0 and s[i] != '0':
                    even += 1
                i += 1
            if zero != len(s) and ((even == 0 and zero == 1) or zero == 0 or math.fmod(sum, 3) != 0):
                print("cyan")
            else:
                print("red")
