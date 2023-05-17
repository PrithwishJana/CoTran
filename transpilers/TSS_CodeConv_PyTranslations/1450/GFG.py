class GFG:
    MAX_CHARS = 256
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSubString(str):
        n = len(str)
        dist_count = 0
        visited = [False for _ in range(GFG.MAX_CHARS)]
        Arrays.fill(visited, False)
        for i in range(0, n):
            if visited [str[i]] == False:
                visited [str[i]] = True
                dist_count += 1
        start = 0
        start_index = - 1
        min_len = Integer.MAX_VALUE
        count = 0
        curr_count = [0 for _ in range(GFG.MAX_CHARS)]
        for j in range(0, n):
            curr_count [str[j]] += 1
            if curr_count [str[j]] == 1:
                count += 1
            if count == dist_count:
                while curr_count [str[start]] > 1:
                    if curr_count [str[start]] > 1:
                        curr_count [str[start]] -= 1
                    start += 1
                len_window = j - start + 1
                if min_len > len_window:
                    min_len = len_window
                    start_index = start
        return str[start_index:start_index + min_len]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "aabcbcdbca"
        print("Smallest window containing all distinct" + " characters is: " + GFG.findSubString(str))
