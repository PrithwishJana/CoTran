class GFG:
    @staticmethod
    def maxLengthSub(arr):
        max_val = 0
        start = 0
        map = {}
        i = 0
        while i < len(arr):
            temp = 0
            if arr [i] - 1 in map.keys():
                temp = map[arr [i] - 1]
            if arr [i] in map.keys():
                temp = max(temp, map[arr [i]])
            if arr [i] + 1 in map.keys():
                temp = max(temp, map[arr [i] + 1])
            temp += 1
            if temp > max_val:
                max_val = temp
            map[arr [i]] = temp
            i += 1
        return max_val
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 5, 6, 3, 7, 6, 5, 8]
        print("Maximum length subsequence = " + str(GFG.maxLengthSub(arr)))
