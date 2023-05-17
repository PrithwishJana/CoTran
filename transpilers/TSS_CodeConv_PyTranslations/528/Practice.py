import math

#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math.min
#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math.max
#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math.abs
class Practice:
    scn = Scanner(System.in)
    sb = StringBuilder()
    out = PrintWriter(System.out)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(HastaLaVistaLa):
        t = 1
        for tests in range(0, t):
            Practice.solve()
        Practice.out.println(Practice.sb)
        Practice.out.close()
    @staticmethod
    def solve():
        n = Practice.scn.nextInt()
        a = [0 for _ in range(n)]
        for i in range(0, n):
            a [i] = Practice.scn.nextInt()
        freq = [0 for _ in range(1010)]
        can = (n + 1)
        for i in a:
            freq [i] += 1
            if freq [i] > math.trunc(can / float(2)):
                Practice.sb.append("NO")
                return
        Practice.sb.append("YES")
