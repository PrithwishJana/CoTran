class GFG:
    @staticmethod
    def fix(A):
        s = HashSet()
        i = 0
        while i < len(A):
            s.add(A [i])
            i += 1
        i = 0
        while i < len(A):
            if s.contains(i):
                A [i] = i
            else:
                A [i] = - 1
            i += 1
        return A
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = [- 1, - 1, 6, 1, 9, 3, 2, - 1, 4, - 1]
        print(Arrays.toString(GFG.fix(A)))
