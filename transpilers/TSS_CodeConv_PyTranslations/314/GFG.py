class GFG:
    @staticmethod
    def Loss(SP, P):
        loss = 0
        loss = float((2 * P * P * SP)) / (100 * 100 - P * P)
        print("Loss = " + "{0:.3f}".format(loss))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        SP = 2400
        P = 30
        GFG.Loss(SP, P)
