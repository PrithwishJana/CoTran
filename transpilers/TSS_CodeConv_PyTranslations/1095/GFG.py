class GFG:
    INT_BITS = 32
    @staticmethod
    def maxSubarrayXOR(set, n):
        index = 0
        for i in range(GFG.INT_BITS - 1, -1, -1):
            maxInd = index
            maxEle = Integer.MIN_VALUE
            for j in range(index, n):
                if (set [j] & (1 << i)) != 0 and set [j] > maxEle:
                    maxEle = set [j]
                    maxInd = j
            if maxEle == - 2147483648:
                continue
            temp = set [index]
            set [index] = set [maxInd]
            set [maxInd] = temp
            maxInd = index
            for j in range(0, n):
                if j != maxInd and (set [j] & (1 << i)) != 0:
                    set [j] = set [j] ^ set [maxInd]
            index += 1
        res = 0
        for i in range(0, n):
            res ^= set [i]
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        set = [9, 8, 5]
        n = len(set)
        print("Max subset XOR is ", end = '')
        print(GFG.maxSubarrayXOR(set, n), end = '')
