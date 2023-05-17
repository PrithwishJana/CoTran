class GFG:
    @staticmethod
    def colourVisible(height, colour, K):
        arr = [0 for _ in range(K + 1)]
        visible = 0
        max = height [K - 1]
        arr [colour [K - 1]] = 1
        for i in range(K - 2, -1, -1):
            if height [i] > max:
                max = height [i]
                arr [colour [i]] = 1
        for i in range(1, K + 1):
            if arr [i] == 1:
                visible += 1
        return visible
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        height = [3, 5, 1, 2, 3]
        colour = [1, 2, 3, 4, 3]
        K = len(colour)
        print(GFG.colourVisible(height, colour, K))
