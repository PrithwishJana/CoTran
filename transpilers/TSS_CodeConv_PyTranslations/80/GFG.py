class GFG:
    NO_OF_CHARS = 256
    @staticmethod
    def max_distinct_char(str, n):
        count = [0 for _ in range(GFG.NO_OF_CHARS)]
        for i in range(0, n):
            count [str[i]] += 1
        max_distinct = 0
        for i in range(0, GFG.NO_OF_CHARS):
            if count [i] != 0:
                max_distinct += 1
        return max_distinct
    @staticmethod
    def smallesteSubstr_maxDistictChar(str):
        n = len(str)
        max_distinct = GFG.max_distinct_char(str, n)
        minl = n
        for i in range(0, n):
            for j in range(0, n):
                subs = None
                if i < j:
                    subs = str[i:j]
                else:
                    subs = str[j:i]
                subs_lenght = len(subs)
                sub_distinct_char = GFG.max_distinct_char(subs, subs_lenght)
                if subs_lenght < minl and max_distinct == sub_distinct_char:
                    minl = subs_lenght
        return minl
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "AABBBCBB"
        len = GFG.smallesteSubstr_maxDistictChar(str)
        print("The length of the smallest substring consisting of maximum distinct characters : " + str(len))
