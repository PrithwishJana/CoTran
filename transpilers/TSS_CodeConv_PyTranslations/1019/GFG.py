class GFG:
    @staticmethod
    def checkTypeOfTriangle(a, b, c):
        sqa = int(a) ** 2
        sqb = int(b) ** 2
        sqc = int(c) ** 2
        if sqa == sqa + sqb or sqb == sqa + sqc or sqc == sqa + sqb:
            print("Right-angled Triangle", end = '')
        elif sqa > sqc + sqb or sqb > sqa + sqc or sqc > sqa + sqb:
            print("Obtuse-angled Triangle", end = '')
        else:
            print("Acute-angled Triangle", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 0
        b = 0
        c = 0
        a = 2
        b = 2
        c = 2
        GFG.checkTypeOfTriangle(a, b, c)
