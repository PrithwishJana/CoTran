class Ratio:
    @staticmethod
    def isRatioPossible(lowCost, upCost, lowQuant, upQuant, r):
        for i in range(lowQuant, upQuant + 1):
            ans = i * r
            if lowCost <= ans and ans <= upCost:
                return True
        return False
    @staticmethod
    def main(args):
        lowCost = 14
        upCost = 30
        lowQuant = 5
        upQuant = 12
        r = 9
        if Ratio.isRatioPossible(lowCost, upCost, lowQuant, upQuant, r):
            print("Yes")
        else:
            print("No")
