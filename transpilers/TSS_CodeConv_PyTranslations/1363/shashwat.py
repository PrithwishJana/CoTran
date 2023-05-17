class shashwat:
    in_ = Scanner(System.in)
    @staticmethod
    def main(args):
        n1 = shashwat.in_.nextInt()
        n2 = shashwat.in_.nextInt()
        x = abs(n1) + abs(n2)
        if n1 >= 0 and n2 >= 0:
            print(str(0) + " " + str(x) + " " + str(x) + " " + str(0))
        elif n1 < 0 and n2 >= 0:
            print("-" + str(x) + " " + str(0) + " " + str(0) + " " + str(x))
        elif n1 < 0 and n2 < 0:
            print("-" + str(x) + " " + str(0) + " " + str(0) + " -" + str(x))
        else:
            print(str(0) + " -" + str(x) + " " + str(x) + " " + str(0))
