class Solution:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = java.util.Scanner(System.in)
        n = in_.nextInt()
        a = [[False for _ in range(11)] for _ in range(4)]
        i = 0
        j = 0
        while n > 0:
            if i == 2 and j != 0:
                i += 1
            a [i][j] = True
            n -= 1
            j += math.trunc(i / float(3))
            i = math.fmod((i + 1), 4)
        print("+------------------------+")
        for i in range(0, 4):
            print("|", end = '')
            for j in range(0, 11):
                print("O." if a [i][j] else (("#." if j == 0 else "..") if i == 2 else "#."), end = '')
            if i == 0:
                print("|D|)")
            else:
                print(("..|" if i == 2 else "|.|") + (")" if i == 3 else ""))
        print("+------------------------+")
