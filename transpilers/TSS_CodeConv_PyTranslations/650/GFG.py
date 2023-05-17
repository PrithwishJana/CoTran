class GFG:
    @staticmethod
    def countElements(p, n):
        ans = 0
        i = 1
        while i < n - 1:
            if p [i - 1] > p [i] and p [i] > p [i + 1]:
                ans += 1
            elif p [i - 1] < p [i] and p [i] < p [i + 1]:
                ans += 1
            i += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        p = [2, 5, 1, 3, 4]
        n = len(p)
        print(GFG.countElements(p, n))
