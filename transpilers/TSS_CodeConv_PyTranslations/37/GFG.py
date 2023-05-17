class GFG:
    N = 3
    @staticmethod
    def MaxTraceSub(mat):
        max_trace = 0
        i = 0
        while i < GFG.N:
            j = 0
            while j < GFG.N:
                r = i
                s = j
                trace = 0
                while r < GFG.N and s < GFG.N:
                    trace += mat [r][s]
                    r += 1
                    s += 1
                    max_trace = max(trace, max_trace)
                j += 1
            i += 1
        return max_trace
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        mat = [[ 10, 2, 5 ], [ 6, 10, 4 ], [ 2, 7, - 10 ]]
        print(GFG.MaxTraceSub(mat))
