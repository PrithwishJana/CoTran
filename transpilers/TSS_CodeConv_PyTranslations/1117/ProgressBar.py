class ProgressBar:
    @staticmethod
    def main(args):
        scan = java.util.Scanner(System.in)
        n = scan.nextInt()
        k = scan.nextInt()
        t = scan.nextInt()
        temp = (t * k * n) / 100.0
        x = 0
        while temp - k >= 0:
            temp -= k
            x += 1
        for i in range(0, x):
            print(str(k) + " ", end = '')
        if temp != 0:
            print(str(int(temp)) + " ", end = '')
            x += 1
        for i in range(x, n):
            print(str(0) + " ", end = '')
        print()
