class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def translate(str):
        len = len(str)
        if len < 2:
            return
        i = 0
        j = 0
        while j < len - 1:
            if str [j] == 'A' and str [j + 1] == 'B':
                j = j + 2
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str [i ++] = 'C';
                str [i ] = 'C'
                i += 1
                continue
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str [i ++] = str [j ++];
            str [i ] = str [j ]
            j += 1
            i += 1
        if j == len - 1:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: str [i ++] = str [j];
            str [i ] = str [j]
            i += 1
        str [i] = ' '
        str [len - 1] = ' '
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        st = "helloABworldABGfG"
        str = st.toCharArray()
        GFG.translate(str)
        print("The modified string is :")
        print(str)
