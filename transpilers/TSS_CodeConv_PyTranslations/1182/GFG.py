class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(a, b):
        l = len(a)
        min = 0
        max = 0
        for i in range(0, l):
            if a [i] == '+' or b [i] == '+' or a [i] != b [i]:
                max += 1
            if a [i] != '+' and b [i] != '+' and a [i] != b [i]:
                min += 1
        print(str(min) + str(max) + "\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s1 = "a+c"
        s2 = "++b"
        GFG.solve(s1.toCharArray(), s2.toCharArray())
