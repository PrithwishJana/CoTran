class GFG:
    @staticmethod
    def q1(s, i):
        if i == len(s):
            print("Yes")
            return
        if s[i] == 'a':
            GFG.q1(s, i + 1)
        else:
            GFG.q2(s, i + 1)
    @staticmethod
    def q2(s, i):
        if i == len(s):
            print("No")
            return
        if s[i] == 'a':
            GFG.q1(s, i + 1)
        else:
            GFG.q2(s, i + 1)
    @staticmethod
    def q3(s, i):
        if i == len(s):
            print("Yes")
            return
        if s[i] == 'a':
            GFG.q4(s, i + 1)
        else:
            GFG.q3(s, i + 1)
    @staticmethod
    def q4(s, i):
        if i == len(s):
            print("No")
            return
        if s[i] == 'a':
            GFG.q4(s, i + 1)
        else:
            GFG.q3(s, i + 1)
    @staticmethod
    def q0(s, i):
        if i == len(s):
            print("No")
            return
        if s[i] == 'a':
            GFG.q1(s, i + 1)
        else:
            GFG.q3(s, i + 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "abbaabb"
        GFG.q0(s, 0)
