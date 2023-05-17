class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(s1, s2):
        mp = {}
        i = 0
        while i < len(s1):
            mp[s1[i]] = 1 if mp[s1[i]] is None else mp[s1[i]] + 1
            i += 1
        i = 0
        while i < len(s2):
            if mp[s2[i]] > 0:
                return True
            i += 1
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s1 = "geeksforgeeks"
        s2 = "geeks"
        yes_or_no = GFG.check(s1, s2)
        if yes_or_no == True:
            print("Yes")
        else:
            print("No")
