class GFG:
    deno = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    N = len(deno)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findMin(V):
        ans = []
        for i in range(GFG.N - 1, -1, -1):
            while V >= GFG.deno [i]:
                V -= GFG.deno [i]
                ans.append(GFG.deno [i])
        for i, unusedItem in enumerate(ans):
            print(ans.elementAt(i) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 93
        print("Following is minimal number of change for " + str(n) + " : ", end = '')
        GFG.findMin(n)
