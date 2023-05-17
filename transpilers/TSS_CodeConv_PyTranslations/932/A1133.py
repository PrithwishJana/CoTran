class A1133:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        x1 = sc.nextInt()
        y1 = sc.nextInt()
        x2 = sc.nextInt()
        y2 = sc.nextInt()
        x3 = sc.nextInt()
        y3 = sc.nextInt()
        print("3")
        print(str(x1 + x2 - x3) + " " + str(y1 + y2 - y3))
        print(str(x3 + x2 - x1) + " " + str(y3 + y2 - y1))
        print(str(x1 + x3 - x2) + " " + str(y1 + y3 - y2))
