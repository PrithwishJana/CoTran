class GFG:
    @staticmethod
    def isSubstring(s1, s2):
        M = len(s1)
        N = len(s2)
        i = 0
        while i <= N - M:
            j = 0
            for j in range(0, M):
                if s2[i + j] != s1[j]:
                    break
            if j == M:
                return i
            i += 1
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s1 = "for"
        s2 = "geeksforgeeks"
        res = GFG.isSubstring(s1, s2)
        if res == - 1:
            print("Not present")
        else:
            print("Present at index " + str(res))
