class Test:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = Scanner(System.in)
        word1 = in_.nextLine().replaceAll("[^a-zA-Z]", "").toLowerCase()
        word2 = in_.nextLine().replaceAll("[^a-zA-Z]", "").toLowerCase()
        word3 = in_.nextLine().replaceAll("[^a-zA-Z]", "").toLowerCase()
        perm1 = word1 + word2 + word3
        perm2 = word1 + word3 + word2
        perm3 = word2 + word1 + word3
        perm4 = word2 + word3 + word1
        perm5 = word3 + word2 + word1
        perm6 = word3 + word1 + word2
        students = in_.nextInt()
        in_.nextLine()
        for i in range(0, students):
            testCase = in_.nextLine().replaceAll("[^a-zA-Z]", "").toLowerCase()
            if testCase == perm1 or testCase == perm2 or testCase == perm3 or testCase == perm4 or testCase == perm5 or testCase == perm6:
                print("ACC")
            else:
                print("WA")
