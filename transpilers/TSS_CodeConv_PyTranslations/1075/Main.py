class solution:
    @staticmethod
    def removeZeros(a, n):
        ind = - 1
        for i in range(0, n):
            if a [i] != 0:
                ind = i
                break
        if ind == - 1:
            print("Array has leading zeros only", end = '')
            return
        b = [0 for _ in range(n - ind)]
        i = 0
        while i < n - ind:
            b [i] = a [ind + i]
            i += 1
        i = 0
        while i < n - ind:
            print(str(b [i]) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [0, 0, 0, 1, 2, 0, 3]
        n = len(a)
        solution.removeZeros(a, n)
