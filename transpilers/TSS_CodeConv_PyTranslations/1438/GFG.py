class GFG:
    @staticmethod
    def commonPrefixUtil(str1, str2):
        result = ""
        n1 = len(str1)
        n2 = len(str2)
        i = 0
        j = 0
        while i <= n1 - 1 and j <= n2 - 1:
            if str1[i] != str2[j]:
                break
            result += str1[i]
            i += 1
            j += 1
        return (result)
    @staticmethod
    def commonPrefix(arr, n):
        arr.sort()
        print(GFG.commonPrefixUtil(arr [0], arr [n - 1]))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
        n = len(arr)
        GFG.commonPrefix(arr, n)
