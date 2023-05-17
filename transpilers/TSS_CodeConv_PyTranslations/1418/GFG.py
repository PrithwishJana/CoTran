import math

class GFG:
    @staticmethod
    def makeEven(string):
        str = string.toCharArray()
        n = len(str)
        even = Integer.MAX_VALUE
        index = 0
        i = 0
        while i < n - 1:
            if math.fmod((str [i] - '0'), 2) == 0:
                even = (str [i] - '0')
                index = i
            if even <= (str [n - 1] - '0'):
                break
            i += 1
        if even == Integer.MAX_VALUE:
            return str
        GFG.swap(str, index, n - 1)
        return str
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def swap(str, index1, index2):
        temp = str [index1]
        str [index1] = str [index2]
        str [index2] = temp
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "1356425"
        print(GFG.makeEven(str), end = '')
