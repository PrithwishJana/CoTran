class GFG:
    @staticmethod
    def areVowelsInOrder(s):
        n = len(s)
        c = chr(64)
        for i in range(1, n):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                if s[i] < c:
                    return False
                else:
                    c = s[i]
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "aabbbddeecc"
        if GFG.areVowelsInOrder(s):
            print("Yes")
        else:
            print("No")
