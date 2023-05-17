class GFG:
    @staticmethod
    def first_subString(s):
        n = len(s)
        c = 0
        s1 = None
        s2 = None
        mpp = {}
        for i in range(0, n):
            if s[i] == ' ' or s[i] == '#':
                s1 = s[c:i]
                mpp[s1] = 1
                c = i + 1
        for i in range(0, n):
            if s[i] == ' ':
                continue
            for j in range(0, n):
                if s[i] == ' ':
                    break
                s1 = s[i:j - i + 1]
                s2 = s1
                s1 = GFG.reverse(s1)
                if s1 in mpp.keys():
                    return s2
        return "-1"
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def reverse(input):
        a = input.toCharArray()
        l = 0
        r = len(a) - 1
        l = 0
        while l < r:
            temp = a [l]
            a [l] = a [r]
            a [r] = temp
            l += 1
            r -= 1
        return str(a)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = None
        s1 = None
        s = "mango is sweet when nam en tastes it#"
        s1 = GFG.first_subString(s)
        print(s1 + "\n", end = '')
