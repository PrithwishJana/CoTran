class GFG:
    @staticmethod
    def nextZero(i, occurrences):
        while i < len(occurrences):
            if occurrences [i] == 0:
                return i
            i += 1
        return - 1
    @staticmethod
    def getModifiedString(str):
        n = len(str)
        if n > 26:
            return "-1"
        ch = str.toCharArray()
        i = 0
        occurrences = [0 for _ in range(26)]
        for i in range(0, n):
            occurrences [ch [i] - 'a'] += 1
        index = GFG.nextZero(0, occurrences)
        for i in range(0, n):
            if occurrences [ch [i] - 'a'] > 1:
                occurrences [ch [i] - 'a'] -= 1
                ch [i] = chr(('a' + index))
                occurrences [index] = 1
                index = GFG.nextZero(index + 1, occurrences)
        return str(ch)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arr):
        str = "geeksforgeeks"
        print(GFG.getModifiedString(str))
