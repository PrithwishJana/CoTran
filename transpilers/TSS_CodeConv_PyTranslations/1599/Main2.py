class Main2:
    v1 = 0
    v2 = 0
    t = 0
    d = 0
    dp = None
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        Main2.v1 = sc.nextInt()
        Main2.v2 = sc.nextInt()
        Main2.t = sc.nextInt()
        Main2.d = sc.nextInt()
        Main2.dp = [[0 for _ in range(1200)] for _ in range(Main2.t)]
        for x in Main2.dp:
            Arrays.fill(x, - 1)
        ans = - 1
        if Main2.t == 2:
            print(Main2.v1 + Main2.v2)
        else:
            print(Main2.v1 + Main2.v2 + Main2.calculate(1, Main2.v1, Main2.v1))
    @staticmethod
    def calculate(currentTime, currentSpeed, prev):
        if currentSpeed < 0:
            return - int((1e8))
        if currentTime == Main2.t - 1:
            if abs(currentSpeed - Main2.v2) <= Main2.d:
                return 0
            return - int((1e8))
        if Main2.dp [currentTime][currentSpeed] != - 1:
            return Main2.dp [currentTime][currentSpeed]
        bestAns = - int((1e8))
        i = 0
        while i <= Main2.d:
            ans = currentSpeed + i + Main2.calculate(currentTime + 1, currentSpeed + i, currentSpeed)
            ans2 = currentSpeed - i + Main2.calculate(currentTime + 1, currentSpeed - i, currentSpeed)
            bestAns = max(bestAns, max(ans, ans2))
            i += 1
        return Main2.dp [currentTime][currentSpeed] = bestAns
