class RobotCleaner:
    @staticmethod
    def time(m, n, rb, cb, rd, cd):
        t = 0
        dr = 1
        dc = 1
        while True:
            if rb == rd or cb == cd:
                return t
            t += 1
            if (rb + dr) <= 0 or (rb + dr > m):
                dr *= - 1
            if (cb + dc) <= 0 or (cb + dc > n):
                dc *= - 1
            rb += dr
            cb += dc
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws Exception
    def main(args):
        streamReader = java.io.InputStreamReader(System.in)
        reader = java.io.BufferedReader(streamReader)
        testCases = int(reader.readLine())
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (testCases -- > 0)
        while testCases  > 0:
            testCases -= 1
            input = reader.readLine().split(" ")
            t = RobotCleaner.time(int(input [0]), int(input [1]), int(input [2]), int(input [3]), int(input [4]), int(input [5]))
            print(t)
        testCases -= 1
