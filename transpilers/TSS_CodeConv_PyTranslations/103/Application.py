class Application:
    @staticmethod
    def main(args):
        scan = java.util.Scanner(System.in)
        n = scan.nextInt()
        for i in range(0, n):
            k = 0
            a = scan.nextInt()
            b = scan.nextInt()
            for j in range(0, a):
                k += scan.nextInt()
            if b == k:
                print("YES")
            else:
                print("NO")
