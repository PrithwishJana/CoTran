class GFG:
    PI = 3.14159265
    @staticmethod
    def area_inscribed(P, B, H):
        return ((P + B - H) * (P + B - H) * (GFG.PI / 4))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        P = 3
        B = 4
        H = 5
        print(GFG.area_inscribed(P, B, H))
