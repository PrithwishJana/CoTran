class geeks:
    @staticmethod
    def countTotalDistinct(str):
        cnt = 0
        items = java.util.HashSet()
        i = 0
        while i < len(str):
            temp = ""
            ans = java.util.HashSet()
            j = i
            while j < len(str):
                temp = temp + str[j]
                ans.add(str[j])
                if not items.contains(temp):
                    items.add(temp)
                    cnt += ans.size()
                j += 1
            i += 1
        return cnt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "ABCA"
        print(geeks.countTotalDistinct(str))
