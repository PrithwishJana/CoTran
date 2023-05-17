class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(n, m, obstacles, range):
        val = min(n, m)
        Arrays.sort(range)
        c = 1
        for i in range(obstacles - 1, -1, -1):
            range [i] = 2 * range [i]
            val -= range [i]
            if val <= 0:
                return c
            else:
                c += 1
        if val > 0:
            return - 1
        return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        m = 5
        obstacles = 3
        range = [1.0, 1.25, 1.15]
        print(str(GFG.solve(n, m, obstacles, range)) + "\n", end = '')
