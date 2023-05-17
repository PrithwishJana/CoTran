class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def translate(str):
        i = 1
        while i < len(str):
            if str [i - 1] == 'A' and str [i] == 'B':
                str [i - 1] = 'C'
                j = 0
                j = i
                while j < len(str) - 1:
                    str [j] = str [j + 1]
                    j += 1
                str [j] = ' '
            i += 1
        return
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        st = "helloABworldABGfG"
        str = st.toCharArray()
        GFG.translate(str)
        print("The modified string is :")
        print(str)
