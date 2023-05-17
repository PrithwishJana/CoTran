class GFG:
    @staticmethod
    def segregate0and1(arr):
        type0 = 0
        type1 = len(arr) - 1
        while type0 < type1:
            if arr [type0] == 1:
                arr [type1] = arr [type1] + arr [type0]
                arr [type0] = arr [type1] - arr [type0]
                arr [type1] = arr [type1] - arr [type0]
                type1 -= 1
            else:
                type0 += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        array = [0, 1, 0, 1, 1, 1]
        GFG.segregate0and1(array)
        print("Array after segregation is ", end = '')
        for a in array:
            print(str(a) + " ", end = '')
