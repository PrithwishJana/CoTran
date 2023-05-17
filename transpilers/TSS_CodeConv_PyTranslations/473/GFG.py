class GFG:
    MAX = 256
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPairs(s):
        cnt = [0 for _ in range(GFG.MAX)]
        i = 0
        while i < len(s):
            cnt [s[i]] += 1
            i += 1
        ans = 0
        i = 0
        while i < GFG.MAX:
            ans += cnt [i] * cnt [i]
            i += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "geeksforgeeks"
        print(GFG.countPairs(s))
