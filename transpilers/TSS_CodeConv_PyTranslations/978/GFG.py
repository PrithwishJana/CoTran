class GFG:
    @staticmethod
    def findMinimumSubsequences(A, B):
        numberOfSubsequences = 1
        sizeOfB = len(B)
        sizeOfA = len(A)
        inf = 1000000
        next = [[0 for _ in range(sizeOfB)] for _ in range(26)]
        for i in range(0, 26):
            for j in range(0, sizeOfB):
                next [i][j] = inf
        for i in range(0, sizeOfB):
            next [B[i] - 'a'][i] = i
        for i in range(0, 26):
            for j in range(sizeOfB - 2, -1, -1):
                if next [i][j] == inf:
                    next [i][j] = next [i][j + 1]
        pos = 0
        i = 0
        while i < sizeOfA:
            if pos == 0 and next [A[i] - 'a'][pos] == inf:
                numberOfSubsequences = - 1
                break
            elif pos < sizeOfB and next [A[i] - 'a'][pos] < inf:
                nextIndex = next [A[i] - 'a'][pos] + 1
                pos = nextIndex
                i += 1
            else:
                numberOfSubsequences += 1
                pos = 0
        return numberOfSubsequences
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = "aacbe"
        B = "aceab"
        print(GFG.findMinimumSubsequences(A, B), end = '')
