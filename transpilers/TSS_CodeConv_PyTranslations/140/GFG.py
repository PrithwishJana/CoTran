class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maximize(A1, A2, n, x, y):
        c = [0 for _ in range(n)]
        sum = 0
        for i in range(0, n):
            c [i] = A2 [i] - A1 [i]
            sum += A1 [i]
        temp = 0
        i = 0
        while i < n - 1:
            if c [i] < c [i + 1]:
                temp = c [i]
                c [i] = c [i + 1]
                c [i + 1] = temp
            i += 1
        maxi = - 1
        for i in range(0, n):
            sum += c [i]
            if i + 1 >= (n - x):
                maxi = max(sum, maxi)
        return maxi
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A1 = [1, 2, 3, 4, 5]
        A2 = [5, 4, 3, 2, 1]
        n = 5
        x = 3
        y = 3
        print(GFG.maximize(A1, A2, n, x, y))
