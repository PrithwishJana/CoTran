class GFG:
    MAX_CHAR = chr(256)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printDistinct(str):
        n = len(str)
        count = [0 for _ in range(GFG.MAX_CHAR)]
        index = [0 for _ in range(GFG.MAX_CHAR)]
        i = 0
        while chr(i) < GFG.MAX_CHAR:
            count [i] = 0
            index [i] = n
            i += 1
        for i in range(0, n):
            x = str[i]
            count [x] += 1
            if count [x] == 1 and x != ' ':
                index [x] = i
            if count [x] == 2:
                index [x] = n
        index.sort()
        i = 0
        while chr(i) < GFG.MAX_CHAR and index [i] != n:
            print(str[index [i]], end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "GeeksforGeeks"
        GFG.printDistinct(str)
