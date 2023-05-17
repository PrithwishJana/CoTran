class GFG:
    @staticmethod
    def countWords(str, len):
        count = 1
        if len == 1:
            return count
        if str[0] == str[1]:
            count *= 1
        else:
            count *= 2
        j = 1
        while j < len - 1:
            if str[j] == str[j - 1] and str[j] == str[j + 1]:
                count *= 1
            elif str[j] == str[j - 1] or str[j] == str[j + 1] or str[j - 1] == str[j + 1]:
                count *= 2
            else:
                count *= 3
            j += 1
        if str[len - 1] == str[len - 2]:
            count *= 1
        else:
            count *= 2
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "abc"
        len = len(str)
        print(GFG.countWords(str, len))
