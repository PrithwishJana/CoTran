import math

class A1581:
    @staticmethod
    def main(args):
        in_ = Scanner(System.in)
        pw = PrintWriter(OutputStreamWriter(System.out))
        n = in_.nextInt()
        arr = [0 for _ in range(n)]
        Arrays.setAll(arr, lambda i : in_.nextInt())
        Arrays.sort(arr)
        if arr [0] == 1:
            pw.println(1)
            pw.close()
            return
        else:
            if n == 1:
                pw.println(arr [0])
                pw.close()
                return
        yes = True
        for i in range(1, n):
            if math.fmod(arr [i], arr [0]) != 0:
                yes = False
                break
        if yes:
            pw.println(arr [0])
        else:
            pw.println(- 1)
        pw.close()
    @staticmethod
    def debug(*obj):
        System.err.println(Arrays.deepToString(obj))
    @staticmethod
    def GCD(a, b):
        if b == 0:
            return a
        else:
            return A1581.GCD(b, math.fmod(a, b))
