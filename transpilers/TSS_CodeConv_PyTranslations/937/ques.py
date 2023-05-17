class ques:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        for j in range(0, n):
            a = sc.nextLong()
            b = sc.nextLong()
            if abs(a - b) == 1:
                print("NO")
            else:
                print("YES")
