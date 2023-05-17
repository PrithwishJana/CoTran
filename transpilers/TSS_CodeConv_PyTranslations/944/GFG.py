class GFG:
    @staticmethod
    def equal_xor_sum(arr, n):
        Sum = 0
        Xor = 0
        for i in range(0, n):
            Sum = Sum + arr [i]
            Xor = Xor ^ arr [i]
        if Sum == Xor:
            print("YES")
        else:
            print("NO")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [6, 3, 7, 10]
        n = len(arr)
        GFG.equal_xor_sum(arr, n)
