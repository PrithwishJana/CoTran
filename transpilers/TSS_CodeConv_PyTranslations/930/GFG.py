import math

class GFG:
    @staticmethod
    def compareStrings(str1, str2):
        i = 0
        while i < len(str1) - 1 and str1[i] == str2[i]:
            i += 1
        if str1[i] > str2[i]:
            return - 1
        if str1[i] < str2[i]:
            return 1
        else:
            return 0
    @staticmethod
    def searchStr(arr, str, first, last):
        if first > last:
            return - 1
        mid = math.trunc((last + first) / float(2))
        if not arr[mid]:
            left = mid - 1
            right = mid + 1
            while True:
                if left < right and right > last:
                    return - 1
                if right <= last and arr[right]:
                    mid = right
                    break
                if left >= right and arr[left]:
                    mid = left
                    break
                right += 1
                left -= 1
        if GFG.compareStrings(str, arr [mid]) == 0:
            return mid
        if GFG.compareStrings(str, arr [mid]) < 0:
            return GFG.searchStr(arr, str, mid + 1, last)
        return GFG.searchStr(arr, str, first, mid - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = ["for", "", "", "", "geeks", "ide", "", "practice", "", "", "quiz", "", ""]
        str = "quiz"
        n = len(arr)
        print(GFG.searchStr(arr, str, 0, n - 1))
