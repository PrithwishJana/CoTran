class GFG:
    @staticmethod
    def pre_process(substrings, s):
        n = len(s)
        count = 0
        for i in range(0, n):
            dup = ""
            for j in range(i, n):
                dup += s[j]
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: substrings [count ++] = dup;
                substrings [count ] = dup
                count += 1
        size = len(substrings)
        i = 0
        while i < size - 1:
            j = i + 1
            while j < len(substrings):
                if substrings[i] > substrings [j]:
                    temp = substrings [i]
                    substrings [i] = substrings [j]
                    substrings [j] = temp
                j += 1
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "geek"
        substrings = [None for _ in range(10)]
        GFG.pre_process(substrings, s)
        queries = [1, 5, 10]
        q = len(queries)
        for i in range(0, q):
            print(substrings [queries [i] - 1])
