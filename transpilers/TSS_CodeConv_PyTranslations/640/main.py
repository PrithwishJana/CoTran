class main:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        input = java.util.Scanner(System.in)
        out = java.io.PrintWriter(System.out)
        n = input.nextInt()
        vec = [[0 for _ in range(4)] for _ in range(n)]
        for i in range(0, n):
            vec [i][0] = input.nextInt()
            vec [i][1] = input.nextInt()
            vec [i][2] = input.nextInt()
            vec [i][3] = input.nextInt()
        ans = 500
        ansprice = 20000
        for i in range(0, n):
            fl = 1
            for j in range(0, n):
                if vec [i][0] < vec [j][0] and vec [i][1] < vec [j][1] and vec [i][2] < vec [j][2]:
                    fl = 0
            if fl == 1:
                if vec [i][3] < ansprice:
                    ansprice = vec [i][3]
                    ans = i + 1
        print(ans)
        out.close()
