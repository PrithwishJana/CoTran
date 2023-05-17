class GFG:
    @staticmethod
    def minIncrementForUnique(A):
        mpp = {}
        for i in A:
            if i in mpp.keys():
                mpp[i] = mpp[i] + 1
            else:
                mpp[i] = 1
        taken = list  ()
        ans = 0
        for x in range(0, 100000):
            if x in mpp.keys() and mpp[x] >= 2:
                taken.append(x * (mpp[x] - 1))
            elif len(taken) > 0 and ((x in mpp.keys() and mpp[x] == 0) or  x not in mpp.keys()):
                ans += x - taken[len(taken) - 1]
                taken.pop(len(taken) - 1)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = [3, 2, 1, 2, 1, 7]
        print(GFG.minIncrementForUnique(A), end = '')
