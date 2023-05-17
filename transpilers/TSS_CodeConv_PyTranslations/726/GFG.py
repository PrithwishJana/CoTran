class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPairs(a, b, n, m):
        cnt = 0
        s = HashSet()
        for i in range(0, n):
            for j in range(0, m):
                sum = a [i] + b [j]
                if s.contains(sum) == False:
                    cnt += 1
                    s.add(sum)
        return cnt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [12, 2, 7]
        n = len(a)
        b = [4, 3, 8]
        m = len(b)
        print(GFG.countPairs(a, b, n, m))
