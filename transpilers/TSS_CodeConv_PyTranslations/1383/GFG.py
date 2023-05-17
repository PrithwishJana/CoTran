class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def totalPairs(s1, s2):
        count = 0
        arr1 = [0 for _ in range(7)]
        arr2 = [0 for _ in range(7)]
        i = 0
        while i < len(s1):
            set_bits = Integer.bitCount(s1[i])
            arr1 [set_bits] += 1
            i += 1
        i = 0
        while i < len(s2):
            set_bits = Integer.bitCount(s2[i])
            arr2 [set_bits] += 1
            i += 1
        for i in range(1, 7):
            count += (arr1 [i] * arr2 [i])
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s1 = "geeks"
        s2 = "forgeeks"
        print(GFG.totalPairs(s1, s2))
