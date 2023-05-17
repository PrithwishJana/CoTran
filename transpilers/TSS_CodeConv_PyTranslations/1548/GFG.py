class GFG:
    @staticmethod
    def findPerm(n, differences):
        ans = list  ()
        ans.clear()
        ans.append(0)
        x = 0
        i = 0
        while i <= n - 2:
            diff = differences[i]
            x = x + diff
            ans.append(x)
            i += 1
        anss = list  ()
        for obj in ans:
            anss.append(obj)
        ans.sort()
        flag = - 1
        i = 1
        while i <= n - 1:
            res = ans[i] - ans[i - 1]
            if res != 1:
                flag = 0
            i += 1
        if flag == 0:
            print(- 1, end = '')
            return
        else:
            mpp = {}
            mpp.clear()
            j = 1
            value_at_index = list  ()
            for x1 in ans:
                mpp[x1] = j
                j += 1
            for x2 in anss:
                value_at_index.append(mpp[x2])
            for x3 in value_at_index:
                print(str(x3) + " ", end = '')
            print()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        differences = list  ()
        differences.append(2)
        differences.append(- 3)
        differences.append(2)
        n = len(differences) + 1
        GFG.findPerm(n, differences)
