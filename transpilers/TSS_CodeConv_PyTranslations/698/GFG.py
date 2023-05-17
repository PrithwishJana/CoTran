class GFG:
    @staticmethod
    def getPairs(a):
        count = 0
        i = 0
        while i < len(a):
            j = 0
            while j < len(a):
                if a [i] < a [j]:
                    count += 1
                j += 1
            i += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [2, 4, 3, 1]
        print(GFG.getPairs(a))
