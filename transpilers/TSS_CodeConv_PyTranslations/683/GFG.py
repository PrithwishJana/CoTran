import math

class GFG:
    @staticmethod
    def AlternateRearrange(arr, n):
        Arrays.sort(arr)
        v1 = []
        v2 = []
        for i in range(0, n):
            if math.fmod(arr [i], 2) == 0:
                v1.append(arr [i])
            else:
                v2.append(arr [i])
        index = 0
        i = 0
        j = 0
        flag = False
        if math.fmod(arr [0], 2) == 0:
            flag = True
        while index < n:
            if flag == True:
                arr [index] = int(v1[i])
                i += 1
                index += 1
                flag = not flag
            else:
                arr [index] = int(v2[j])
                j += 1
                index += 1
                flag = not flag
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [9, 8, 13, 2, 19, 14]
        n = len(arr)
        GFG.AlternateRearrange(arr, n)
