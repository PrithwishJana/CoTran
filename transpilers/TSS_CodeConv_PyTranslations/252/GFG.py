import math

class GFG:
    @staticmethod
    def cal_IST(h, r):
        IST = (h * r * 1.0) / 360
        int_IST = int(IST)
        float_IST = int(math.ceil(int(((IST - int_IST) * 60))))
        print(str(int_IST) + ":" + str(float_IST))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        h = 20
        r = 150
        GFG.cal_IST(h, r)
