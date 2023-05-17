class A:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.in_ = None

    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        with Scanner(System.in) as in_, java.io.PrintWriter(System.out) as out:
            n = self.in_.nextInt()
            a = []
            for i in range(0, n):
                value = self.in_.nextInt()
                a.append(value)
            a = a.stream().distinct().sorted().collect(java.util.stream.Collectors.toList())
            found = False
            for i, unusedItem in enumerate(a):
                if i + 1 < len(a) and i + 2 < len(a):
                    if a[i] + 1 == a[i + 1] and a[i + 1] + 1 == a[i + 2]:
                        found = True
            out.println("YES" if found else "NO")
