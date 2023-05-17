class GFG:
    @staticmethod
    def missingNum(arr, n):
        list = list(len(arr))
        for i in arr:
            list.append(i)
        minvalue = Collections.min(list)
        pass
        xornum = 0
        for i in range(0, n):
            xornum ^= (minvalue) ^ arr [i]
            minvalue += 1
        return xornum ^ minvalue
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [13, 12, 11, 15]
        n = len(arr)
        print(GFG.missingNum(arr, n))
