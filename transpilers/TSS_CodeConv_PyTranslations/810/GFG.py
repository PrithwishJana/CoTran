class GFG:
    MAX = 1000
    @staticmethod
    def replaceSpaces(str):
        space_count = 0
        i = 0
        i = 0
        while i < len(str):
            if str [i] == ' ':
                space_count += 1
            i += 1
        while str [i - 1] == ' ':
            space_count -= 1
            i -= 1
        new_length = i + space_count * 2
        if new_length > GFG.MAX:
            return str
        index = new_length - 1
        new_str = str
        str = ['\0' for _ in range(new_length)]
        for j in range(i - 1, -1, -1):
            if new_str [j] == ' ':
                str [index] = '0'
                str [index - 1] = '2'
                str [index - 2] = '%'
                index = index - 3
            else:
                str [index] = new_str [j]
                index -= 1
        return str
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "Mr John Smith " .toCharArray()
        str = GFG.replaceSpaces(str)
        i = 0
        while i < len(str):
            print(str [i], end = '')
            i += 1
