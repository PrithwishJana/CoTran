class Solution:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        m = sc.nextInt()
        if n == 0:
            if m != 0:
                print("Impossible")
            else:
                print(str(0) + " " + str(0))
            return
        if m <= n:
            if m == 0:
                m = 1
            print(str(n) + " " + str(m + n - 1), end = '')
            return
        print(str(m) + " " + str(m + n - 1), end = '')
