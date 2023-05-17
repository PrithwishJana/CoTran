class GFG:
    @staticmethod
    def find_maxm(arr, n):
        mp = {}
        for i in range(0, n):
            if arr [i] in mp.keys():
                mp[arr [i]] = mp[arr [i]] + 1
            else:
                mp[arr [i]] = 1
        ans = 0
        for x in mp.entrySet():
            value = x.getKey()
            freq = x.getValue()
            if value == freq:
                ans = max(ans, value)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 2, 2, 3, 4, 3]
        n = len(arr)
        print(GFG.find_maxm(arr, n), end = '')
