class GFG:
    @staticmethod
    def MinDeletion(a, n):
        mp = {}
        for i in range(0, n):
            if a [i] in mp.keys():
                mp[a [i]] = mp[a [i]] + 1
            else:
                mp[a [i]] = 1
        ans = 0
        for i in mp.entrySet():
            x = i.getKey()
            frequency = i.getValue()
            if x <= frequency:
                ans += (frequency - x)
            else:
                ans += frequency
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [2, 3, 2, 3, 4, 4, 4, 4, 5]
        n = len(a)
        print(GFG.MinDeletion(a, n))
