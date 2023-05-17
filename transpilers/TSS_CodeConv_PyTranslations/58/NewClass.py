class NewClass:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        name1 = in_.next()
        name2 = in_.next()
        print(name1 + " " + name2)
        n = in_.nextInt()
        while True:
            s1 = in_.next()
            s2 = in_.next()
            if s1 == name1:
                name1 = s2
            if s1 == name2:
                name2 = s2
            print(name1 + " " + name2)
            n -= 1
            if n == 0:
                break
