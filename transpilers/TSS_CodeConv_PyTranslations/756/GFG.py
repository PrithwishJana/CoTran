class GFG:
    @staticmethod
    def frequency(a, n, x):
        count = 0
        for i in range(0, n):
            if a [i] == x:
                count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [0, 5, 5, 5, 4]
        x = 5
        n = len(a)
        print(GFG.frequency(a, n, x))
