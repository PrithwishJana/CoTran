class GFG:
    @staticmethod
    def bitAtGivenPosSetOrUnset(n, k):
        new_num = n >> (k - 1)
        return (new_num & 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        k = 2
        if GFG.bitAtGivenPosSetOrUnset(n, k) == 1:
            print("Set")
        else:
            print("Unset")
