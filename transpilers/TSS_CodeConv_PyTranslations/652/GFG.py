class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findVolume(l, b, h):
        volume = (l * b * h) / 2
        return volume
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        l = 18
        b = 12
        h = 9
        print("Volume of triangular prism: " + str(GFG.findVolume(l, b, h)))
