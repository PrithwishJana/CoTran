class GFG:
    @staticmethod
    def increaseInVol(l, b, h):
        percentInc = (1 + (l / 100)) * (1 + (b / 100)) * (1 + (h / 100))
        percentInc -= 1
        percentInc *= 100
        return percentInc
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        l = 50
        b = 20
        h = 10
        print(str(GFG.increaseInVol(l, b, h)) + "%")
