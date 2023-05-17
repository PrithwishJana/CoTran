class GFG:
    NO_OF_CHARS = 256
    @staticmethod
    def getSecondMostFreq(str):
        count = [0 for _ in range(GFG.NO_OF_CHARS)]
        i = 0
        i = 0
        while i < len(str):
            (count [str[i]]) += 1
            i += 1
        first = 0
        second = 0
        for i in range(0, GFG.NO_OF_CHARS):
            if count [i] > count [first]:
                second = first
                first = i
            elif count [i] > count [second] and count [i] != count [first]:
                second = i
        return chr(second)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeksforgeeks"
        res = GFG.getSecondMostFreq(str)
        if res != '\0':
            print("Second most frequent char" + " is " + res)
        else:
            print("No second most frequent" + "character")
