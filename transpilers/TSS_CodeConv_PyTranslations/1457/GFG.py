class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countFreq(arr, n):
        mp = {}
        for i in range(0, n):
            mp[arr [i]] = 1 if mp[arr [i]] is None else mp[arr [i]] + 1
        for i in range(0, n):
            if mp[arr [i]] != - 1:
                print(str(arr [i]) + " " + str(mp[arr [i]]))
                mp[arr [i]] = - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 20, 20, 10, 10, 20, 5, 20]
        n = len(arr)
        GFG.countFreq(arr, n)
