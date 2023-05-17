class GFG:
    MAX = 26
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def max_element(freq):
        max_ele = freq [0]
        i = 0
        while i < GFG.MAX:
            if max_ele < freq [i]:
                max_ele = freq [i]
            i += 1
        return max_ele
    @staticmethod
    def minimumAddition(str, len):
        freq = [0 for _ in range(GFG.MAX)]
        for i in range(0, len):
            freq [str[i] - 'a'] += 1
        maxFreq = GFG.max_element(freq)
        minAddition = 0
        i = 0
        while i < GFG.MAX:
            if freq [i] > 0:
                minAddition += abs(maxFreq - freq [i])
            i += 1
        return minAddition
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeksforgeeks"
        len = len(str)
        print(GFG.minimumAddition(str, len))
