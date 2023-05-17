class cf1535A:
    @staticmethod
    def main(args):
        input = Scanner(System.in)
        t = input.nextInt()
        for i in range(1, t + 1):
            a = [0 for _ in range(4)]
            for k in range(0, 4):
                a [k] = input.nextInt()
            if max(a [0], a [1]) > min(a [2], a [3]) and max(a [2], a [3]) > min(a [0], a [1]):
                print("YES")
            else:
                print("NO")
