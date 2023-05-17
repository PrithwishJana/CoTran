class A_FindDivisible:
    @staticmethod
    def main(args):
        scanner = java.util.Scanner(System.in)
        f = None
        t = 0
        l = None
        r = None
        t = scanner.nextInt()
        while t > 0:
            try:
                l = scanner.next()
                r = scanner.next()
                print(l + " " + str(int(l) * 2))
                t -= 1
            except Exception as e:
                System.exit(0)
        System.exit(0)
