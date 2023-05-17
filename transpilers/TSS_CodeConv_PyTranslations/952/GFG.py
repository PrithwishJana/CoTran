class GFG:
    @staticmethod
    def getSingle(arr, n):
        ones = 0
        twos = 0
        common_bit_mask = 0
        for i in range(0, n):
            twos = twos | (ones & arr [i])
            ones = ones ^ arr [i]
            common_bit_mask = ~ (ones & twos)
            ones &= common_bit_mask
            twos &= common_bit_mask
        return ones
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 3, 2, 3]
        n = len(arr)
        print("The element with single occurrence is " + str(GFG.getSingle(arr, n)))
