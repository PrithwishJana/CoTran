class App:
    @staticmethod
    def main(args):
        color = "blue"
        locked = False
        in_ = java.util.Scanner(System.in)
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final int lines = in.nextInt();
        lines = in_.nextInt()
        for i in range(0, lines):
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final String next = in.next();
            next = in_.next()
            if "lock" == next.intern():
                locked = True
                continue
            if "unlock" == next.intern():
                locked = False
                continue
            if locked:
                continue
            color = next
        print(color)
