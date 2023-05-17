import math

class GFG:
    @staticmethod
    def addToArrayForm(A, K):
        v = []
        ans = []
        rem = 0
        i = 0
        for i in range(len(A) - 1, -1, -1):
            my = A[i] + math.fmod(K, 10) + rem
            if my > 9:
                rem = 1
                v.append(math.fmod(my, 10))
            else:
                v.append(my)
                rem = 0
            K = math.trunc(K / float(10))
        while K > 0:
            my = math.fmod(K, 10) + rem
            v.append(math.fmod(my, 10))
            if math.trunc(my / float(10)) > 0:
                rem = 1
            else:
                rem = 0
            K = math.trunc(K / float(10))
        if rem > 0:
            v.append(rem)
        for j in range(len(v) - 1, -1, -1):
            ans.append(v[j])
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = []
        A.append(2)
        A.append(7)
        A.append(4)
        K = 181
        ans = GFG.addToArrayForm(A, K)
        for i, unusedItem in enumerate(ans):
            print(ans[i], end = '')
