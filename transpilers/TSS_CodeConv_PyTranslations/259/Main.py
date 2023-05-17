import math

class MinSwaps:
    @staticmethod
    def findAllSequences(diff, out, start, end):
        if abs(diff) > math.trunc((end - start + 1) / float(2)):
            return
        if start > end:
            if diff == 0:
                print(str(out, 0, len(out) - 1), end = '')
                print(" ", end = '')
            return
        out [start] = '0'
        out [end] = '1'
        MinSwaps.findAllSequences(diff + 1, out, start + 1, end - 1)
        out [start] = out [end] = '1'
        MinSwaps.findAllSequences(diff, out, start + 1, end - 1)
        out [start] = out [end] = '0'
        MinSwaps.findAllSequences(diff, out, start + 1, end - 1)
        out [start] = '1'
        out [end] = '0'
        MinSwaps.findAllSequences(diff - 1, out, start + 1, end - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 2
        out = ['\0' for _ in range(2 * n + 1)]
        out [2 * n] = '\0'
        MinSwaps.findAllSequences(0, out, 0, 2 * n - 1)
        print("")
