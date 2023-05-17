import math

class Lesson:
    sc = Scanner(System.in)
    @staticmethod
    def check(sb):
        t = 0
        i = 0
        while i < sb.length():
            if sb.charAt(i) is "T":
                t += 1
            elif sb.charAt(i) is "M":
                if t <= 0:
                    return False
                t -= 1
            i += 1
        return True
    @staticmethod
    def main(*args):
        t = Lesson.sc.nextInt()
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java labels and gotos:
#        OUTER_LOOP :
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = Lesson.sc.nextInt()
            sb = StringBuilder(Lesson.sc.next())
            if sb.indexOf("M") < 0:
                print("NO")
                continue
            T = 0
            m = 0
            i = 0
            while i < sb.length():
                if sb.charAt(i) is "T":
                    T += 1
                else:
                    m += 1
                i += 1
            if math.trunc(T / float(2)) != m:
                print("NO")
                continue
            if Lesson.check(sb) == True and Lesson.check(sb.reverse()) == True:
                print("YES")
            else:
                print("NO")
        t -= 1
