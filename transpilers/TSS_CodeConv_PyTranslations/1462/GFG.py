class GFG:
    @staticmethod
    def unique_combination(l, sum, K, local, A):
        if sum == K:
            print("{", end = '')
            for i, unusedItem in enumerate(local):
                if i != 0:
                    print(" ", end = '')
                print(local[i], end = '')
                if i != len(local) - 1:
                    print(", ", end = '')
            print("}")
            return
        for i in range(l, len(A)):
            if sum + A[i] > K:
                continue
            if i == 1 and A[i] is A[i - 1] and i > l:
                continue
            local.append(A[i])
            GFG.unique_combination(i + 1, sum + A[i], K, local, A)
            local.pop(len(local) - 1)
    @staticmethod
    def Combination(A, K):
        A.sort()
        local = list  ()
        GFG.unique_combination(0, 0, K, local, A)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 1, 2, 7, 6, 1, 5]
        A = list(Arrays.asList(arr))
        K = 8
        GFG.Combination(A, K)
