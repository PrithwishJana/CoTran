class GfG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def print(a, n, ind):
        b = ['\0' for _ in range((2 * n))]
        for i in range(0, n):
            b [i] = b [n + i] = a [i]
        i = ind
        while i < n + ind:
            print(b [i] + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(argc):
        a = ['A', 'B', 'C', 'D', 'E', 'F']
        n = 6
        GfG.print(a, n, 3)
