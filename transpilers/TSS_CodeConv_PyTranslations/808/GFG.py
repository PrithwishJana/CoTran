class GFG:
    @staticmethod
    def XandYandZintercept(A, B, C, D):
        rslt = [0 for _ in range(3)]
        x = - D / A
        y = - D / B
        z = - D / C
        rslt [0] = x
        rslt [1] = y
        rslt [2] = z
        return rslt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = 2
        B = 5
        C = 7
        D = 8
        rslt = GFG.XandYandZintercept(A, B, C, D)
        print(Arrays.toString(rslt))
