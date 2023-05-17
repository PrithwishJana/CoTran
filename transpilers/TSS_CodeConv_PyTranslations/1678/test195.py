class test195:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        n = in_.nextInt()
        a = in_.next().toCharArray()
        b = in_.next().toCharArray()
        sum = 0
        for i in range(0, n):
            if abs(a [i] - b [i]) > 5:
                sum += 10 - abs(a [i] - b [i])
            else:
                sum += abs(a [i] - b [i])
        print(sum)
        in_.close()
