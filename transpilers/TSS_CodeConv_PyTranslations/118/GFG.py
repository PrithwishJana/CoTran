class GFG:
    @staticmethod
    def isAnyNotPalindrome(s):
        unique = HashSet()
        i = 0
        while i < len(s):
            unique.add(s[i])
            i += 1
        if unique.size() > 1:
            return True
        else:
            return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "aaaaab"
        if GFG.isAnyNotPalindrome(s):
            print("YES")
        else:
            print("NO")
