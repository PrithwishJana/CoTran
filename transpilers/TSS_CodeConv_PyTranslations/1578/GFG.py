class GFG:
    @staticmethod
    def longLenSub(arr, n):
        um = {}
        longLen = 0
        for i in range(0, n):
            len = 0
            if arr [i] - 1 in um.keys() and len < um[arr [i] - 1]:
                len = um[arr [i] - 1]
            if arr [i] + 1 in um.keys() and len < um[arr [i] + 1]:
                len = um[arr [i] + 1]
            um[arr [i]] = len + 1
            if longLen < um[arr [i]]:
                longLen = um[arr [i]]
        return longLen
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 4, 5, 3, 2]
        n = len(arr)
        print("Longest length subsequence = " + str(GFG.longLenSub(arr, n)))
