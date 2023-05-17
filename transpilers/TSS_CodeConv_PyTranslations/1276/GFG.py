class GFG:
    NO_OF_CHARS = 256
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSubString(str, pat):
        len1 = len(str)
        len2 = len(pat)
        if len1 < len2:
            print("No such window exists")
            return ""
        hash_pat = [0 for _ in range(GFG.NO_OF_CHARS)]
        hash_str = [0 for _ in range(GFG.NO_OF_CHARS)]
        for i in range(0, len2):
            hash_pat [pat[i]] += 1
        start = 0
        start_index = - 1
        min_len = Integer.MAX_VALUE
        count = 0
        for j in range(0, len1):
            hash_str [str[j]] += 1
            if hash_pat [str[j]] != 0 and hash_str [str[j]] <= hash_pat [str[j]]:
                count += 1
            if count == len2:
                while hash_str [str[start]] > hash_pat [str[start]] or hash_pat [str[start]] == 0:
                    if hash_str [str[start]] > hash_pat [str[start]]:
                        hash_str [str[start]] -= 1
                    start += 1
                len_window = j - start + 1
                if min_len > len_window:
                    min_len = len_window
                    start_index = start
        if start_index == - 1:
            print("No such window exists")
            return ""
        return str[start_index:start_index + min_len]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "this is a test string"
        pat = "tist"
        print("Smallest window is :\n " + GFG.findSubString(str, pat), end = '')
