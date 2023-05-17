class GFG:
    @staticmethod
    def findUniquePair(arr, n):
        XOR = arr [0]
        for i in range(1, n):
            XOR = XOR ^ arr [i]
        set_bit_no = XOR & ~ (XOR - 1)
        x = 0
        y = 0
        for i in range(0, n):
            if (arr [i] & set_bit_no) > 0:
                x = x ^ arr [i]
            else:
                y = y ^ arr [i]
        print("The unique pair is (" + str(x) + ", " + str(y) + ")")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [6, 1, 3, 5, 1, 3, 7, 6]
        n = len(a)
        GFG.findUniquePair(a, n)
