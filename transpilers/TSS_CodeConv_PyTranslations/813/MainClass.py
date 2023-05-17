class MainClass:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(agrs):
        sc = java.util.Scanner(System.in)
        a = sc.nextInt()
        b = sc.nextInt()
        if a == b:
            print(str(a * 10) + str(1) + " " + str(a * 10 + 2))
        elif a + 1 == b:
            print(str(a) + " " + str(b))
        elif a + 1 == b * 10:
            print(str(a) + " " + str(b * 10))
        else:
            print(- 1)
