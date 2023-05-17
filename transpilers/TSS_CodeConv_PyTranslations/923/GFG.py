class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def pattern(min_stars, p_height):
        p_space = 0
        p_space = p_height - 1
        i = 0
        j = 0
        k = 0
        n = 0
        x = 0
        x = 1
        for i in range(0, p_height):
            for j in range(p_space, i, -1):
                print(" ", end = '')
            for k in range(0, min_stars):
                print("*", end = '')
            for n in range((p_height + p_height - 2), x - 1, -1):
                print(" ", end = '')
            for k in range(0, min_stars):
                print("*", end = '')
            min_stars = min_stars + 2
            x = x + 2
            print()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        min_stars = 1
        p_height = 5
        GFG.pattern(min_stars, p_height)
