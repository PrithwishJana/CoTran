import math

class GFG:
    @staticmethod
    def findWinner(n):
        if math.fmod((n - 1), 6) == 0:
            print("Second Player wins the game")
        else:
            print("First Player wins the game")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 7
        GFG.findWinner(n)
