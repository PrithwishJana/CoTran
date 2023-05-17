class CF:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = Scanner(System.in)
        pw = PrintWriter(System.out)
        test = in_.nextInt()
        for t in range(0, test):
            n = in_.nextInt()
            k = in_.nextInt()
            list = []
            for i in range(0, n):
                v = in_.nextInt()
                list.append(v)
            list.sort()
            div = 1
            count = 0
            sum = 0
            for i in range(n - 1, -1, -1):
                sum += list[i]
                if sum / (div * 1.0) >= k:
                    count += 1
                    div += 1
                else:
                    break
            pw.println(count)
        pw.close()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def debug(*obj):
        System.err.println(Arrays.deepToString(obj))
