class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPoints(n, m, a, b, x, y):
        Arrays.sort(a)
        Arrays.sort(b)
        j = 0
        count = 0
        for i in range(0, n):
            while j < m:
                if a [i] + y < b [j]:
                    break
                if b [j] >= a [i] - x and b [j] <= a [i] + y:
                    count += 1
                    j += 1
                    break
                else:
                    j += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 1
        y = 4
        a = [1, 5]
        n = len(a)
        b = [1, 1, 2]
        m = len(a)
        print(GFG.countPoints(n, m, a, b, x, y))
