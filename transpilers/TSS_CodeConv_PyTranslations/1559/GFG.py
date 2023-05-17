class GFG:
    @staticmethod
    def isHeterogram(s, n):
        hash = [0 for _ in range(26)]
        for i in range(0, n):
            if s[i] != ' ':
                if hash [s[i] - 'a'] == 0:
                    hash [s[i] - 'a'] = 1
                else:
                    return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "the big dwarf only jumps"
        n = len(s)
        if GFG.isHeterogram(s, n):
            print("YES", end = '')
        else:
            print("NO", end = '')
